# -*- coding: utf-8 -*-
"""
Created on Fri May 16 2025
@author: Jon Carlstedt Tønnessen aka joncto

Description:
Cyber Attack is a text-based command-line interface game where you play as a web archiving team, trying to preserve the web for future generations.
"""


import sys

def show_title():
    ascii_title = r"""


                                                                                                                                                         
   @@@@@@@*  @@@    @@  @@@@@@@@@   @@@@@@@@  @@@@@@@@@          @@@@     @@@@@@@@@    @@@@@@@@   @@      @@   @@  @@      @@  @@   @@@@@@@: @@@@@@@@@@  
  @@     =@@  @@@  @@   @@#    @@:  @@        @@@    @@-         @@@@@    @@*    @@   @@      @@  @@      @@   @@  @@@    @@   @@  @@=    @@     @@      
 @@-           @@@@@    @@@@@@@@@   @@@@@@@@  @@@   @@@         @@  @@    @@*   @@@  @@@          @@@@@@@@@@   @@   @@   @@*   @@   @@@@@        @@      
 @@-            *@@     @@#    @@@  @@        @@@@@@@@         @@@%%%@@   @@@@@@@@   @@@          @@      @@   @@    @@  @@    @@       @@@@     @@      
  @@      @@     @@     @@#     @@  @@        @@@    @@       .@@    @@@  @@*    @@   @@      @@  @@      @@   @@    @@@@@     @@  @@     *@@    @@      
   @@@@@@@@      @@     @@@@@@@@@   @@@@@@@@= @@@     @@      @@      @@  @@*    *@@   @@@@@@@@   @@      @@   @@     @@@@     @@   @@@@@@@@     @@      
                                                                                                                                                         

                                                                 
"""
    print(ascii_title)

def ask_choice(prompt, choices):
    print(prompt)
    for key, value in choices.items():
        print(f"{key}) {value}")
    while True:
        choice = input("> ").strip().lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def crawl_and_store():
    print("\nPhase 1: Crawl and Store to WARC")
    choices = {
        'a': "Crawl all big news sites",
        'b': "Crawl a personal blog about knives",
        'c': "Let an unsupervised AI curate the crawl"
    }
    choice = ask_choice("What would you like to crawl?", choices)

    print()
    if choice == 'a':
        print("RESULT: Crawl successful, but some JavaScript failed to render.")
        return 7
    elif choice == 'b':
        print("RESULT: You archived a complete blog, including images and metadata. Your boss is questioning if maybe the news would be more important.")
        return 10
    elif choice == 'c':
        print("RESULT: The AI archived 5,000 cookie popups and missed the main content.")
        return 3

def index_for_replay():
    print("\nPhase 2: Indexing for Replay")
    choices = {
        'a': "Manually review all content before putting it into the CDX",
        'b': "Auto-index with pywb",
        'c': "Use AI to predict missing entries"
    }
    choice = ask_choice("Choose your indexing strategy:", choices)

    print()
    if choice == 'a':
        print("RESULT: Manual review ensured high quality, but only for the 120 pages you had time for. None of them were of interest to the end user.")
        return 10
    elif choice == 'b':
        print("RESULT: Content is searchable and curators can assess that the content has been archived.")
        return 5
    elif choice == 'c':
        print("RESULT: AI hallucinated and made up new MIME types. Replay is unusable.")
        return 4

def perform_quality_assessment():
    print("\nPhase 3: Perform Quality Assessment")
    choices = {
        'a': "Use visual replay for a sample of pages that were collected",
        'b': "Rely on automated QA logs only",
        'c': "Skip QA and publish openly"
    }
    choice = ask_choice("How will you assess quality?", choices)

    print()
    if choice == 'a':
        print("RESULT: You found some errors that improves future crawls. Ready for preservation and end-users!")
        return 10
    elif choice == 'b':
        print("RESULT: In three years, you will discover that you missed all content that depended on behaviour. But for now, you can live blissfully ignorant.")
        return 6
    elif choice == 'c':
        print("RESULT: Significant replay issues. Luckily, people saw it and made you aware of the problems, improving future crawls.")
        return 2

def develop_research_services():
    print("\nPhase 4: Develop Research Services")
    choices = {
        'a': "Build full-text search with citation tools",
        'b': "Offer simple URL search",
        'c': "Setup a ChatBot using OpenAI to summarize all archived pages"
    }
    choice = ask_choice("Choose your service model:", choices)

    print()
    if choice == 'a':
        print("RESULT: Researchers are thrilled. Your archive is cited in several major studies and headlines the Library's Annual Report.")
        return 10
    elif choice == 'b':
        print("RESULT: Internal staff are super happy. But external end-users require a lot of training, stopping any human curation for 6 months.")
        return 6
    elif choice == 'c':
        print("RESULT: Summaries are fast but misleading. Trust in the web archive declines and the Head of the Library wants to change the whole team.")
        return 3

def final_score(total, team_name):
    print("\nFinal Report:")
    print(f"Archiving Team: {team_name}")
    print(f"Total Preservation Score: {total} / 40")
    if total >= 36:
        print("Outstanding work! Your archive will be remembered for generations.")
    elif total >= 28:
        print("Solid effort. Some gaps exist, but your contribution is significant.")
    elif total >= 16:
        print("Mixed results. Important materials were preserved, but quality suffered.")
    else:
        print("The archive is fragile. Key records are lost or untrustworthy.")

def wait_to_continue():
    input("\nPress Enter to continue...")

def play_game():
    show_title()
    print("Welcome to CYBER ARCHIVIST!")
    team_name = input("Enter the name of your archiving team: ")
    print(f"\nTeam '{team_name}', your mission is to collect and preserve the web for research and documentation. Good luck!\n")

    score = 0
    score += crawl_and_store()
    wait_to_continue()
    score += index_for_replay()
    wait_to_continue()
    score += perform_quality_assessment()
    wait_to_continue()
    score += develop_research_services()
    wait_to_continue()
    final_score(score, team_name)

if __name__ == "__main__":
    play_game()

