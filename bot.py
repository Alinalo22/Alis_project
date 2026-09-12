from rubpy.bot import BotClient, filters

app = BotClient("CECIGI0DCWRXMAIYWEEXQKFOXOTJZLUWBSDVDSHECCRANQLCBSKLDKMGOJDWZANM")

ADMIN_ID = "u0IZVwo085c2a0fc27583c26b22ad271"
GROUP_LINK = "https://rubika.ir/joing/JBBBJGFG0YWLOTWAUWUIYTSTJILSXDLI"

QUESTIONS = [
    "اسم شما چیست؟",
    "سن شما چند است؟",
    "آیدی روبیکای خود را وارد کنید:",
    "اسم شما در بازی چیست؟"
]

user_states = {}
pending_forms = {}

@app.on_update(filters.text)
async def handler(client, update):
    user_id = update.new_message.sender_id
    text = update.new_message.text

    if text == "/forms":
        if user_id == ADMIN_ID:
            if not pending_forms:
                await update.reply("هیچ فرم جدیدی وجود ندارد.")
            else:
                for uid, form in list(pending_forms.items()):
                    report = f"فرم جدید از {uid}:\n\n"
                    for i, q in enumerate(QUESTIONS):
                        report += f"{q}\n{form['answers'][i]}\n\n"
                    report += f"برای تایید: /approve_{uid}\n"
                    report += f"برای لغو: /reject_{uid}"
                    await update.reply(report)
        return

    if text.startswith("/approve_"):
        if user_id == ADMIN_ID:
            target_user_id = text.replace("/approve_", "")
            if target_user_id in pending_forms:
                form = pending_forms[target_user_id]
                try:
                    await app.send_message(
                        chat_id=form["chat_id"],
                        text=f"🎉 تبریک! درخواست شما تایید شد.\n\n🔗 لینک گروه:\n{GROUP_LINK}"
                    )
                    await update.reply(f"✅ کاربر تایید شد و لینک برای او ارسال گردید.")
                    del pending_forms[target_user_id]
                except Exception as e:
                    await update.reply(f"خطا در ارسال به کاربر: {e}")
            else:
                await update.reply("اطلاعات این کاربر یافت نشد.")
        return

    if text.startswith("/reject_"):
        if user_id == ADMIN_ID:
            target_user_id = text.replace("/reject_", "")
            if target_user_id in pending_forms:
                form = pending_forms[target_user_id]
                try:
                    await app.send_message(
                        chat_id=form["chat_id"],
                        text="❌ متاسفانه درخواست شما تایید نشد."
                    )
                    await update.reply(f"❌ کاربر لغو شد و پیام برای او ارسال گردید.")
                    del pending_forms[target_user_id]
                except Exception as e:
                    await update.reply(f"خطا در ارسال به کاربر: {e}")
            else:
                await update.reply("اطلاعات این کاربر یافت نشد.")
        return

    if text == "/start":
        user_states[user_id] = {"step": 0, "answers": []}
        await update.reply(QUESTIONS[0])
        return

    if user_id in user_states and user_states[user_id]["step"] < len(QUESTIONS):
        user_states[user_id]["answers"].append(text)
        next_step = user_states[user_id]["step"] + 1

        if next_step < len(QUESTIONS):
            user_states[user_id]["step"] = next_step
            await update.reply(QUESTIONS[next_step])
        else:
            answers = user_states[user_id]["answers"]
            pending_forms[user_id] = {
                "chat_id": update.chat_id,
                "answers": answers
            }
            await update.reply("پاسخ‌های شما ثبت شد. مدیریت بررسی خواهد کرد.")
            del user_states[user_id]

app.run()
