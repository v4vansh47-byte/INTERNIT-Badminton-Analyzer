import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def create_large_database():
    """
    Generates a comprehensive database for 15 NITs (75 players) and
    a 5-year historical ranking of the INTER-NIT tournament.
    """
    # --- 5-Year INTER-NIT Historical Rankings ---
    # Based on user input and realistic progression.
    historical_rankings = {
        'Year 2024': ['1. NIT Trichy', '2. VNIT Nagpur', '3. NIT Surathkal'],
        'Year 2023': ['1. VNIT Nagpur', '2. SVNIT Surat', '3. NIT Surathkal'],
        'Year 2022': ['1. SVNIT Surat', '2. NIT Trichy', '3. NIT Kurukshetra'],
        'Year 2021': ['1. NIT Warangal', '2. VNIT Nagpur', '3. SVNIT Surat'],
        'Year 2020': ['1. NIT Surathkal', '2. NIT Warangal', '3. NIT Rourkela']
    }

    # --- College Player Database (75 Players from 15 NITs) ---
    # Stats are generated to reflect team strength and historical rankings.
    college_data = [
        # Tier 1 Teams (Frequent Podium Finishers)
        # NIT Trichy (Strong, 2024 Champions)
        {'player_name': 'Arjun Menon', 'college': 'NIT Trichy', 'tournaments_played': 8, 'matches_won': 32, 'finals_reached': 7, 'trophies_won': 5},
        {'player_name': 'Karthik S.', 'college': 'NIT Trichy', 'tournaments_played': 7, 'matches_won': 28, 'finals_reached': 5, 'trophies_won': 3},
        {'player_name': 'Sriram Iyer', 'college': 'NIT Trichy', 'tournaments_played': 6, 'matches_won': 22, 'finals_reached': 4, 'trophies_won': 2},
        {'player_name': 'Prakash Rao', 'college': 'NIT Trichy', 'tournaments_played': 5, 'matches_won': 18, 'finals_reached': 2, 'trophies_won': 2},
        {'player_name': 'Ganesh Kumar', 'college': 'NIT Trichy', 'tournaments_played': 4, 'matches_won': 15, 'finals_reached': 1, 'trophies_won': 1},

        # VNIT Nagpur (Strong, 2023 Champions)
        {'player_name': 'Aditya Joshi', 'college': 'VNIT Nagpur', 'tournaments_played': 8, 'matches_won': 30, 'finals_reached': 6, 'trophies_won': 4},
        {'player_name': 'Rohan Patil', 'college': 'VNIT Nagpur', 'tournaments_played': 7, 'matches_won': 27, 'finals_reached': 5, 'trophies_won': 3},
        {'player_name': 'Prathamesh S.', 'college': 'VNIT Nagpur', 'tournaments_played': 6, 'matches_won': 21, 'finals_reached': 3, 'trophies_won': 2},
        {'player_name': 'Mihir Kulkarni', 'college': 'VNIT Nagpur', 'tournaments_played': 5, 'matches_won': 17, 'finals_reached': 2, 'trophies_won': 1},
        {'player_name': 'Sanket Deshmukh', 'college': 'VNIT Nagpur', 'tournaments_played': 4, 'matches_won': 14, 'finals_reached': 1, 'trophies_won': 1},

        # NIT Surathkal (Consistent Top 3)
        {'player_name': 'Vikram Shenoy', 'college': 'NIT Surathkal', 'tournaments_played': 9, 'matches_won': 31, 'finals_reached': 7, 'trophies_won': 3},
        {'player_name': 'Anand Hegde', 'college': 'NIT Surathkal', 'tournaments_played': 8, 'matches_won': 26, 'finals_reached': 5, 'trophies_won': 2},
        {'player_name': 'Manoj Kamath', 'college': 'NIT Surathkal', 'tournaments_played': 7, 'matches_won': 23, 'finals_reached': 4, 'trophies_won': 2},
        {'player_name': 'Rajesh Shetty', 'college': 'NIT Surathkal', 'tournaments_played': 6, 'matches_won': 19, 'finals_reached': 3, 'trophies_won': 1},
        {'player_name': 'Dinesh Pai', 'college': 'NIT Surathkal', 'tournaments_played': 5, 'matches_won': 16, 'finals_reached': 2, 'trophies_won': 1},

        # SVNIT Surat (Strong, 2022 Champions)
        {'player_name': 'Parth Patel', 'college': 'SVNIT Surat', 'tournaments_played': 8, 'matches_won': 29, 'finals_reached': 6, 'trophies_won': 3},
        {'player_name': 'Keval Shah', 'college': 'SVNIT Surat', 'tournaments_played': 7, 'matches_won': 25, 'finals_reached': 4, 'trophies_won': 2},
        {'player_name': 'Meet Desai', 'college': 'SVNIT Surat', 'tournaments_played': 6, 'matches_won': 20, 'finals_reached': 3, 'trophies_won': 2},
        {'player_name': 'Harsh Mehta', 'college': 'SVNIT Surat', 'tournaments_played': 5, 'matches_won': 15, 'finals_reached': 2, 'trophies_won': 1},
        {'player_name': 'Dhruv Gandhi', 'college': 'SVNIT Surat', 'tournaments_played': 4, 'matches_won': 12, 'finals_reached': 1, 'trophies_won': 0},
        
        # NIT Warangal (Strong, 2021 Champions)
        {'player_name': 'Srinivas Reddy', 'college': 'NIT Warangal', 'tournaments_played': 9, 'matches_won': 28, 'finals_reached': 5, 'trophies_won': 3},
        {'player_name': 'Naveen Kumar', 'college': 'NIT Warangal', 'tournaments_played': 8, 'matches_won': 24, 'finals_reached': 4, 'trophies_won': 2},
        {'player_name': 'Venkat Prasad', 'college': 'NIT Warangal', 'tournaments_played': 7, 'matches_won': 21, 'finals_reached': 3, 'trophies_won': 1},
        {'player_name': 'Sai Charan', 'college': 'NIT Warangal', 'tournaments_played': 6, 'matches_won': 18, 'finals_reached': 2, 'trophies_won': 1},
        {'player_name': 'Kiran Raj', 'college': 'NIT Warangal', 'tournaments_played': 5, 'matches_won': 15, 'finals_reached': 1, 'trophies_won': 0},

        # Tier 2 Teams (Strong Contenders)
        # NIT Kurukshetra (Your Team, on the podium in 2022)
        {'player_name': 'Tarun Sharma', 'college': 'NIT Kurukshetra', 'tournaments_played': 6, 'matches_won': 18, 'finals_reached': 3, 'trophies_won': 2},
        {'player_name': 'Vansh', 'college': 'NIT Kurukshetra', 'tournaments_played': 5, 'matches_won': 15, 'finals_reached': 2, 'trophies_won': 1},
        {'player_name': 'Chaitanya Verma', 'college': 'NIT Kurukshetra', 'tournaments_played': 5, 'matches_won': 12, 'finals_reached': 1, 'trophies_won': 1},
        {'player_name': 'Hitesh Kumar', 'college': 'NIT Kurukshetra', 'tournaments_played': 4, 'matches_won': 9, 'finals_reached': 1, 'trophies_won': 0},
        {'player_name': 'Rahul Singh', 'college': 'NIT Kurukshetra', 'tournaments_played': 3, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},

        # NIT Rourkela (Podium in 2020)
        {'player_name': 'Anirban Das', 'college': 'NIT Rourkela', 'tournaments_played': 7, 'matches_won': 20, 'finals_reached': 3, 'trophies_won': 1},
        {'player_name': 'Sourav Mohanty', 'college': 'NIT Rourkela', 'tournaments_played': 6, 'matches_won': 17, 'finals_reached': 2, 'trophies_won': 1},
        {'player_name': 'Pritam Sahoo', 'college': 'NIT Rourkela', 'tournaments_played': 5, 'matches_won': 14, 'finals_reached': 1, 'trophies_won': 0},
        {'player_name': 'Bikash Jena', 'college': 'NIT Rourkela', 'tournaments_played': 4, 'matches_won': 11, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Subham Mishra', 'college': 'NIT Rourkela', 'tournaments_played': 3, 'matches_won': 8, 'finals_reached': 0, 'trophies_won': 0},
        
        # NIT Calicut
        {'player_name': 'Fahad Mohammed', 'college': 'NIT Calicut', 'tournaments_played': 6, 'matches_won': 16, 'finals_reached': 2, 'trophies_won': 0},
        {'player_name': 'Nihal Krishnan', 'college': 'NIT Calicut', 'tournaments_played': 5, 'matches_won': 13, 'finals_reached': 1, 'trophies_won': 0},
        {'player_name': 'Abin George', 'college': 'NIT Calicut', 'tournaments_played': 5, 'matches_won': 11, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Roshan P.M.', 'college': 'NIT Calicut', 'tournaments_played': 4, 'matches_won': 9, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Jithin Jose', 'college': 'NIT Calicut', 'tournaments_played': 3, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},

        # MANIT Bhopal
        {'player_name': 'Ayush Tiwari', 'college': 'MANIT Bhopal', 'tournaments_played': 6, 'matches_won': 15, 'finals_reached': 1, 'trophies_won': 0},
        {'player_name': 'Harsh Saxena', 'college': 'MANIT Bhopal', 'tournaments_played': 5, 'matches_won': 12, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Rajat Sharma', 'college': 'MANIT Bhopal', 'tournaments_played': 4, 'matches_won': 10, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Shivam Dubey', 'college': 'MANIT Bhopal', 'tournaments_played': 4, 'matches_won': 8, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Prateek Jain', 'college': 'MANIT Bhopal', 'tournaments_played': 3, 'matches_won': 5, 'finals_reached': 0, 'trophies_won': 0},

        # Tier 3 Teams (Developing Teams)
        # NIT Jalandhar
        {'player_name': 'Gurpreet Singh', 'college': 'NIT Jalandhar', 'tournaments_played': 5, 'matches_won': 10, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Manpreet Brar', 'college': 'NIT Jalandhar', 'tournaments_played': 4, 'matches_won': 8, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Sandeep Kumar', 'college': 'NIT Jalandhar', 'tournaments_played': 4, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Karan Malhotra', 'college': 'NIT Jalandhar', 'tournaments_played': 3, 'matches_won': 4, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Amit Bhalla', 'college': 'NIT Jalandhar', 'tournaments_played': 2, 'matches_won': 2, 'finals_reached': 0, 'trophies_won': 0},

        # NIT Delhi
        {'player_name': 'Mohit Yadav', 'college': 'NIT Delhi', 'tournaments_played': 4, 'matches_won': 9, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Ankit Sharma', 'college': 'NIT Delhi', 'tournaments_played': 4, 'matches_won': 7, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Sahil Aggarwal', 'college': 'NIT Delhi', 'tournaments_played': 3, 'matches_won': 5, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Vipul Bansal', 'college': 'NIT Delhi', 'tournaments_played': 2, 'matches_won': 3, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Nitin Garg', 'college': 'NIT Delhi', 'tournaments_played': 2, 'matches_won': 2, 'finals_reached': 0, 'trophies_won': 0},

        # NIT Jamshedpur
        {'player_name': 'Abhishek Kumar', 'college': 'NIT Jamshedpur', 'tournaments_played': 5, 'matches_won': 11, 'finals_reached': 1, 'trophies_won': 0},
        {'player_name': 'Ritesh Singh', 'college': 'NIT Jamshedpur', 'tournaments_played': 4, 'matches_won': 8, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Suraj Prasad', 'college': 'NIT Jamshedpur', 'tournaments_played': 3, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Chandan Mahto', 'college': 'NIT Jamshedpur', 'tournaments_played': 3, 'matches_won': 4, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Vivek Gupta', 'college': 'NIT Jamshedpur', 'tournaments_played': 2, 'matches_won': 3, 'finals_reached': 0, 'trophies_won': 0},

        # NIT Durgapur
        {'player_name': 'Arijit Banerjee', 'college': 'NIT Durgapur', 'tournaments_played': 4, 'matches_won': 8, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Sayan Roy', 'college': 'NIT Durgapur', 'tournaments_played': 4, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Debjit Ghosh', 'college': 'NIT Durgapur', 'tournaments_played': 3, 'matches_won': 5, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Rahul Das', 'college': 'NIT Durgapur', 'tournaments_played': 2, 'matches_won': 3, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Arnab Mondal', 'college': 'NIT Durgapur', 'tournaments_played': 2, 'matches_won': 2, 'finals_reached': 0, 'trophies_won': 0},
        
        # NIT Goa
        {'player_name': 'Akshay Naik', 'college': 'NIT Goa', 'tournaments_played': 4, 'matches_won': 7, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Rohit Prabhu', 'college': 'NIT Goa', 'tournaments_played': 3, 'matches_won': 5, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Siddharth Gaude', 'college': 'NIT Goa', 'tournaments_played': 3, 'matches_won': 4, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Varun Fernandes', 'college': 'NIT Goa', 'tournaments_played': 2, 'matches_won': 3, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Neel Kamat', 'college': 'NIT Goa', 'tournaments_played': 2, 'matches_won': 2, 'finals_reached': 0, 'trophies_won': 0},

        # NIT Srinagar
        {'player_name': 'Aaqib Bhat', 'college': 'NIT Srinagar', 'tournaments_played': 3, 'matches_won': 6, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Umar Farooq', 'college': 'NIT Srinagar', 'tournaments_played': 3, 'matches_won': 4, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Zubair Wani', 'college': 'NIT Srinagar', 'tournaments_played': 2, 'matches_won': 3, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Faizan Mir', 'college': 'NIT Srinagar', 'tournaments_played': 2, 'matches_won': 2, 'finals_reached': 0, 'trophies_won': 0},
        {'player_name': 'Adil Shah', 'college': 'NIT Srinagar', 'tournaments_played': 1, 'matches_won': 1, 'finals_reached': 0, 'trophies_won': 0},
    ]
    college_df = pd.DataFrame(college_data)
    return college_df, historical_rankings

def calculate_player_strength(player_stats):
    """Calculates a single 'Strength Score' based on a player's achievements."""
    if player_stats is None:
        return 0  # Handle the case where player_stats might be None
    weights = {
        'trophies_won': 25, 'finals_reached': 10, 'matches_won': 2, 'tournaments_played': 1
    }
    score = (player_stats['trophies_won'] * weights['trophies_won'] +
             player_stats['finals_reached'] * weights['finals_reached'] +
             player_stats['matches_won'] * weights['matches_won'] +
             player_stats['tournaments_played'] * weights['tournaments_played'])
    return score

def predict_college_match(p1_stats, p2_stats):
    s1 = calculate_player_strength(p1_stats)
    s2 = calculate_player_strength(p2_stats)
    if s1 + s2 == 0: return 0.5
    return s1 / (s1 + s2)

def predict_team_matchup(team1_roster, team2_roster, simulations=10000):
    print(f"\nSimulating {team1_roster['college'].iloc[0]} vs {team2_roster['college'].iloc[0]}...")
    print("Format: Best-of-5 Singles Matchup (Top 5 players from each team)")
    team1_wins = 0
    num_matches = min(len(team1_roster), len(team2_roster), 5)
    for i in range(simulations):
        t1_match_wins, t2_match_wins = 0, 0
        for j in range(num_matches):
            p1_stats, p2_stats = team1_roster.iloc[j], team2_roster.iloc[j]
            p1_win_prob = predict_college_match(p1_stats, p2_stats)
            if np.random.rand() < p1_win_prob:
                t1_match_wins += 1
            else:
                t2_match_wins += 1
        if t1_match_wins >= 3:
            team1_wins += 1
    return team1_wins / simulations

def plot_prediction_graph(name1, prob1, name2, prob2, title):
    names = [name1, name2]
    probabilities = [prob1 * 100, prob2 * 100]
    colors = ['#4CAF50', '#F44336']
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(names, probabilities, color=colors)
    ax.set_ylabel('Win Probability (%)', fontsize=12)
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    ax.tick_params(axis='x', labelsize=12)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points",
                     ha='center', va='bottom', fontsize=14, fontweight='bold')
    plt.figtext(0.5, 0.01, 'Disclaimer: This is a simulation based on historical data, not a real-time prediction.',
                ha='center', fontsize=8, style='italic', color='gray')
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

def display_historical_rankings(rankings):
    print("\n" + "="*45)
    print("         INTER-NIT Badminton Rankings (Last 5 Years)")
    print("="*45)
    for year, podium in rankings.items():
        print(f"\n🏆 {year}:")
        for rank in podium:
            print(f"  {rank}")
    print("="*45)

def select_player_from_db(college_db, prompt_text="Choose a player"):
    """Improved player selection UI."""
    colleges = college_db['college'].unique()
    print(f"\n--- {prompt_text} ---")
    
    while True:
        print("First, select a college:")
        for i, name in enumerate(colleges):
            print(f"{i+1}. {name}")
        try:
            college_idx = int(input("Choose a college number: ")) - 1
            if 0 <= college_idx < len(colleges):
                chosen_college = colleges[college_idx]
                break
            else:
                print("Invalid college number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player_roster = college_db[college_db['college'] == chosen_college].reset_index(drop=True)
    
    while True:
        print(f"\nNow, select a player from {chosen_college}:")
        for i, row in player_roster.iterrows():
            print(f"{i+1}. {row['player_name']}")
        try:
            player_idx = int(input("Choose a player number: ")) - 1
            if 0 <= player_idx < len(player_roster):
                return player_roster.iloc[player_idx]
            else:
                print("Invalid player number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_my_stats(my_name, my_college):
    print(f"\nEnter stats for {my_name} ({my_college}):")
    stats = {'player_name': my_name, 'college': my_college}
    prompts = {
        'tournaments_played': ("Total tournaments played: ", int),
        'matches_won': ("Total official matches won: ", int),
        'finals_reached': ("Number of times reached a final: ", int),
        'trophies_won': ("Number of trophies/medals won: ", int)
    }
    for key, (prompt, type_func) in prompts.items():
        while True:
            try:
                stats[key] = type_func(input(prompt))
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    return stats

def main():
    college_db, historical_rankings = create_large_database()
    my_name = ""
    my_college = "NIT Kurukshetra"

    print("🏸" * 25)
    print("   Welcome to the INTER-NIT Badminton Analyzer!")
    print("         (Professional Edition)")
    print("🏸" * 25)

    while True:
        print("\n--- Main Menu ---")
        print("1. Compare College Players (Singles Match)")
        print("2. Predict INTER-NIT Team Matchup")
        print("3. View INTER-NIT Historical Rankings")
        print("4. Add/Update My Stats & Compare Myself")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            p1_stats = select_player_from_db(college_db, "Select Player 1")
            p2_stats = select_player_from_db(college_db, "Select Player 2")
            
            win_prob = predict_college_match(p1_stats, p2_stats)
            print("\n--- Prediction Analysis ---")
            print(f"{p1_stats['player_name']} Strength Score: {calculate_player_strength(p1_stats):.0f}")
            print(f"{p2_stats['player_name']} Strength Score: {calculate_player_strength(p2_stats):.0f}\n")
            
            plot_prediction_graph(
                p1_stats['player_name'], win_prob,
                p2_stats['player_name'], 1 - win_prob,
                f"Match Prediction: {p1_stats['player_name']} vs {p2_stats['player_name']}"
            )
        
        elif choice == '2':
            colleges = college_db['college'].unique()
            print("\n--- Select Teams for INTER-NIT Matchup ---")
            
            while True:
                for i, name in enumerate(colleges): print(f"{i+1}. {name}")
                try:
                    t1_idx = int(input("Choose Team 1: ")) - 1
                    if 0 <= t1_idx < len(colleges):
                        t1_name = colleges[t1_idx]
                        break
                    else:
                        print("Invalid team number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    t2_idx = int(input("Choose Team 2: ")) - 1
                    if 0 <= t2_idx < len(colleges) and t2_idx != t1_idx: # Ensure different teams are selected
                        t2_name = colleges[t2_idx]
                        break
                    else:
                        print("Invalid team number or same as Team 1. Please choose a different team.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            team1_roster = college_db[college_db['college'] == t1_name].sort_values('matches_won', ascending=False).reset_index(drop=True)
            team2_roster = college_db[college_db['college'] == t2_name].sort_values('matches_won', ascending=False).reset_index(drop=True)
            
            team_win_prob = predict_team_matchup(team1_roster, team2_roster)
            
            plot_prediction_graph(
                t1_name, team_win_prob,
                t2_name, 1 - team_win_prob,
                f"Team Matchup Prediction (Best-of-5)"
            )

        elif choice == '3':
            display_historical_rankings(historical_rankings)

        elif choice == '4':
            if not my_name: my_name = input("Enter your name: ")
            my_stats_data = get_my_stats(my_name, my_college)
            
            # Remove existing entry for 'my_name' if it exists before adding updated stats
            college_db = college_db[college_db['player_name'] != my_name].copy() 
            
            my_stats_df = pd.DataFrame([my_stats_data])
            college_db = pd.concat([college_db, my_stats_df], ignore_index=True)
            
            print(f"\nWelcome, {my_name}! Your stats have been added. Now, let's compare.")
            my_full_stats = college_db[college_db['player_name'] == my_name].iloc[0]
            opp_stats = select_player_from_db(college_db[college_db['player_name'] != my_name], "Select an Opponent")

            win_prob = predict_college_match(my_full_stats, opp_stats)
            print("\n--- Your Match Analysis ---")
            print(f"Your Strength Score: {calculate_player_strength(my_full_stats):.0f}")
            print(f"{opp_stats['player_name']}'s Strength Score: {calculate_player_strength(opp_stats):.0f}\n")
            
            plot_prediction_graph(
                f"You ({my_name})", win_prob,
                opp_stats['player_name'], 1 - win_prob,
                f"Match Prediction: You vs {opp_stats['player_name']}"
            )

        elif choice == '5':
            print("\nGood luck in the upcoming tournaments! Exiting program.")
            break
        else:
            print("\nInvalid choice. Please select from the menu.")
            
        print("\n" + "="*40)
        time.sleep(1)

if __name__ == "__main__":
    main()
