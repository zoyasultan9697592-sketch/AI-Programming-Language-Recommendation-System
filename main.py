from colorama import Fore, init
from datetime import datetime
import time

from data import recommendations, careers, roadmaps, resources, salary
from functions import typing_effect, loading_animation

init(autoreset=True)


print(Fore.GREEN+ "=" *70)
typing_effect("          💻 AI PROGRAMMING LANGUAGE RECOMMENDATION SYSTEM", Fore.CYAN)
print(Fore.GREEN+ "=" *70,"\n")


typing_effect("👤 USER PROFILE", Fore.YELLOW)
print(Fore.GREEN+ "-"*40)

name = input(Fore.MAGENTA+ "Enter your Name:")

print()

typing_effect(f"🎉🥰WELCOME {name}", Fore.CYAN)

print(Fore.GREEN + "=" * 70)
print()


now = datetime.now()

typing_effect(f"📅 Date: {now.strftime('%d-%m-%Y')}", Fore.YELLOW)
typing_effect(f"🕒 Time : {now.strftime('%I:%M:%S %p')}", Fore.YELLOW)

print(Fore.GREEN+ "="*70)
print()


running = True


while running:

    typing_effect("Choose your Interset:", Fore.YELLOW)
    print(Fore.GREEN+"-"*40)

    typing_effect("1. Web development")
    typing_effect("2. Artificial Intelligence")
    typing_effect("3. Data science")
    typing_effect("4. Cyber security")
    typing_effect("5. Mobile Development")

    print()

    try:
        choice = int(input(Fore.LIGHTMAGENTA_EX+ "Enter your choice(1-5):"))

    except:
        typing_effect("❌ Please enter numbers only!", Fore.RED)
        continue


    if choice == 1:
        interest="web development"

    elif choice == 2:
        interest="artificial intelligence"

    elif choice == 3:
        interest="data science"

    elif choice == 4:
        interest="cyber security"

    elif choice == 5:
        interest="mobile development"

    else:
        interest=None



    typing_effect("Select Your Skill Level", Fore.YELLOW)

    print(Fore.GREEN + "-" * 40)

    typing_effect("1. Beginner")
    typing_effect("2. Intermediate")
    typing_effect("3. Advanced")


    print()


    try:
        level = int(input(Fore.LIGHTMAGENTA_EX+ "Enter your level(1-3):"))

    except:
        typing_effect("❌ Please enter numbers only!", Fore.RED)
        continue

    if level == 1:
        skill_level = "Beginner"

    elif level == 2:
        skill_level = "Intermediate"

    elif level == 3:
        skill_level = "Advanced"

    else:
        skill_level = None


    print()


    typing_effect("🤖 AI is analyzing your profile...", Fore.YELLOW)


    loading_animation()


    typing_effect("✅ ANALYSIS COMPLETE", Fore.GREEN)

    print()


    typing_effect(f"🎯 Your Skill Level: {skill_level}", Fore.CYAN)


    if interest:


        print(Fore.GREEN + "╔" + "═"*55 + "╗")
        print(Fore.GREEN + "║" + Fore.CYAN + "      💻 RECOMMENDED PROGRAMMING LANGUAGES      " + Fore.GREEN + "║")
        print(Fore.GREEN + "╠" + "═"*55 + "╣")


        for language in recommendations[interest][skill_level]:

            typing_effect("✅ " + language, Fore.YELLOW)
            time.sleep(0.1)


        print(Fore.GREEN + "╚" + "═"*55 + "╝")


    else:

        typing_effect("❌ Invalid Choice!", Fore.RED)


    print()


    typing_effect("💼 Recommended Career Paths", Fore.MAGENTA)

    print(Fore.GREEN + "-" * 40)


    for career in careers[interest]:

        typing_effect("✔ " + career, Fore.CYAN)
        time.sleep(0.1)


    print()


    typing_effect("💰 ESTIMATED SALARY", Fore.YELLOW)

    print(Fore.GREEN + "=" * 70)


    typing_effect(salary[interest], Fore.CYAN)


    print(Fore.GREEN + "=" * 70)


    print()


    typing_effect("🛣️ Learning Roadmap", Fore.YELLOW)

    print(Fore.GREEN + "-" * 40)


    step = 1


    for item in roadmaps[interest]:

        typing_effect(f"Step {step}: {item}", Fore.CYAN)

        step += 1

        time.sleep(0.1)


    print()


    typing_effect("📚 Best Learning Resources", Fore.BLUE)

    print(Fore.GREEN + "-" * 40)


    for resource in resources[interest]:

        typing_effect("🌐 " + resource, Fore.YELLOW)

        time.sleep(0.1)



    print()

    print(Fore.GREEN + "╔" + "═"*50 + "╗")
    print(Fore.GREEN + "║            📋 USER SUMMARY            ║")
    print(Fore.GREEN + "╠" + "═"*50 + "╣")


    typing_effect(f" Interest     : {interest}", Fore.CYAN)

    typing_effect(f" Skill Level  : {skill_level}", Fore.CYAN)

    typing_effect(f" Total Skills : {len(recommendations[interest][skill_level])}", Fore.CYAN)


    print(Fore.GREEN + "╚" + "═"*50 + "╝")


    print()


    again = input("🔄 Do you want another recommendation? (yes/no): ").lower()


    if again != "yes":

        running = False

        typing_effect("👋 Thank you for using the AI Recommendation System!", Fore.CYAN)