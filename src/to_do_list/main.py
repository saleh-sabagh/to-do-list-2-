from dotenv import load_dotenv
from cli import show_menu, input_choice, input_project_name, input_project_description, \
    input_task_title, input_task_description, input_task_deadline
from controller import choose_project, choose_task, edit_project, edit_task
from project import Project

load_dotenv()


def main() -> None:
    """Run the main loop of the TO DO List Manager."""
    while True:
        show_menu()
        choice = input_choice()

        try:
            if choice == "1":
                Project(input_project_name(), input_project_description())
                print("✅ Project created successfully.")

            elif choice == "2":
                project, _ = choose_project()
                if not project:
                    continue
                project.add_task(input_task_title(), input_task_description(), input_task_deadline())
                print(f"✅ Task added to {project.name}.")

            elif choice == "3":
                project, _ = choose_project()
                if project:
                    edit_project(project)

            elif choice == "4":
                project, _ = choose_project()
                if project:
                    task = choose_task(project)
                    if task:
                        edit_task(task)

            elif choice == "5":
                project, _ = choose_project()
                if project:
                    task = choose_task(project)
                    if task:
                        project.remove_task(task.id)
                        print("✅ Task deleted successfully!!")

            elif choice == "6":
                projects = [(p.id, p.name, p.description) for p in Project.all_projects().values()]
                if projects:
                    print("\n📂 Your Projects:")
                    print("=" * 50)
                    for pid, name, desc in projects:
                        print(f"🆔 ID         : {pid}")
                        print(f"📁 Name       : {name}")
                        print(f"📝 Description: {desc}")
                        print("-" * 50)
                else:
                    print("⚠️  There are no projects yet!")
                print("_____________________")

            elif choice == "7":
                project, _ = choose_project()
                if project:
                    tasks = [(t.id, t.title, t.description,t.deadline, t.status) for t in project.all_project_tasks().values()]
                    if tasks:
                        print("\n📋 Tasks in Project:")
                        print("=" * 50)
                        for tid, title, desc, deadline, status in tasks:
                            short_desc = desc if len(desc) < 100 else desc[:100] + "..."
                            print(f"🆔 Task ID     : {tid}")
                            print(f"📌 Title       : {title}")
                            print(f"📝 Description : {short_desc}")
                            print(f"🕒 Deadline    : {deadline}")
                            print(f"📊 Status      : {status}")
                            print("-" * 50)
                    else:
                        print("⚠️  There are no tasks in this project.")
                print()

            elif choice == "8":
                project, project_name = choose_project()
                if project:
                    Project.delete_project(project_name)
                    print("✅ Project deleted successfully!")

            elif choice == "0":
                print("👋 Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()
