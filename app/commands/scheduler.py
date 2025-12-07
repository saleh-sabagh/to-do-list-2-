# app/commands/scheduler.py
import time
import schedule
from app.commands.autoclose_overdue import autoclose_overdue
from app.db.session import get_db_session
from datetime import datetime

def job_autoclose():
    with get_db_session() as session:
        count = autoclose_overdue(session)
        print(f"[scheduler] {datetime.now().isoformat()} closed {count} tasks")

def main():
    # مثال: اجرا هر 15 دقیقه
    schedule.every(15).minutes.do(job_autoclose)

    # یا هر روز ساعت 00:00:
    # schedule.every().day.at("00:00").do(job_autoclose)

    print("[scheduler] started")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
