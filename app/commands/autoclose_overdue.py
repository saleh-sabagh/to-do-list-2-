# app/commands/autoclose_overdue.py
from datetime import datetime
from typing import List

from app.db.session import get_db_session
from app.models.task import Task
from sqlalchemy.orm import Session

def autoclose_overdue(session: Session) -> int:
    """
    Mark tasks overdue as done (status = "done") and set closed_at.
    Returns number of tasks updated.
    """
    now = datetime.now()
    # پیدا کردن تسک‌هایی که deadline کمتر از الان دارند و هنوز done نیستند
    overdue_tasks: List[Task] = session.query(Task).filter(
        Task.deadline.is_not(None),
        Task.deadline < now,
        Task.status != "done"
    ).all()

    count = 0
    for task in overdue_tasks:
        task.status = "done"
        task.closed_at = now
        # اگر نیاز است لاگ یا عملیات اضافی اضافه کنید اینجا انجام شود
        count += 1

    if count:
        session.commit()
    else:
        # اگر تغییری نبوده است، rollback لازم نیست ولی می‌توان session.flush() یا commit() نزنی
        session.rollback()

    return count


def main():
    # این تابع را می‌توان از CLI یا cron صدا زد
    with get_db_session() as session:
        updated = autoclose_overdue(session)
        print(f"[autoclose-overdue] {updated} tasks closed at {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
