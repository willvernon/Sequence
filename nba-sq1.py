# 1) Current Team Tier Level 'Tier 1 = 5pts', 'T2 = 3pts', 'T3 = 1pts'
# 2) Past 4 Games played; T1 Win = 5, T2 = 3, T3 - 1, 
#   a) Add 2pts for T1 Away Win, or 1pts for T2 Away Win, no added for T3
# 3) Compare team starters 1pt for each better player
# 4) Current Home Team gets 3pts
def alg(last_game):
    points = 0

    if last_game == "t1wa":
        points += 7
    elif last_game == "t1wh":
        points += 5
    elif last_game == "t2wa":
        points += 4
    elif last_game == "t2wh":
        points += 3
    elif last_game == "t3wa":
        points += 1
    elif last_game == "t3wh":
        points += 1

    return points

def tier_points(team_tier):
    points = 0

    if team_tier == "t1":
        points += 5
    elif team_tier == "t2":
        points += 3
    elif team_tier == "t3":
        points += 1
    
    return points

def main():
    team1_ttl = 0
    team2_ttl = 0

    team1_name = input("Enter Team 1: ")
    team_tier = input("Enter Team Tier (t1,t2,t3): ")
    team1_ttl += tier_points(team_tier)
    current_gm_home = input("Home Team in Comparison (y/n): ")
    if current_gm_home == 'y':
        team1_ttl += 2
    else:
        team2_ttl += 2
    tm1_last_game1 = input("Enter Last Game 1 (t1wh, t1la, etc.): ")
    team1_ttl += alg(tm1_last_game1)
    tm1_last_game2 = input("Enter Last Game 2 (t1wh, t1la, etc.): ")
    team1_ttl += alg(tm1_last_game2)
    tm1_last_game3 = input("Enter Last Game 3 (t1wh, t1la, etc.): ")
    team1_ttl += alg(tm1_last_game3)
    tm1_last_game4 = input("Enter Last Game 4 (t1wh, t1la, etc.): ")
    team1_ttl += alg(tm1_last_game4)

    team2_name = input("Enter Team 2: ")
    team_tier2 = input("Enter Team2 Tier (t1,t2,t3): ")
    team2_ttl += tier_points(team_tier2)
    tm2_last_game1 = input("Enter Last Game 1 (t1wh, t1la, etc.): ")
    team2_ttl += alg(tm2_last_game1)
    tm2_last_game2 = input("Enter Last Game 2 (t1wh, t1la, etc.): ")
    team2_ttl += alg(tm2_last_game2)
    tm2_last_game3 = input("Enter Last Game 3 (t1wh, t1la, etc.): ")
    team2_ttl += alg(tm2_last_game3)
    tm2_last_game4 = input("Enter Last Game 4 (t1wh, t1la, etc.): ")
    team2_ttl += alg(tm2_last_game4)

    pg_comp = input("Who Has Better PG (team1, team2): ")
    if pg_comp == "team1":
        team1_ttl += 1 
    else:
        team2_ttl += 1 
   
    sg_comp = input("Who Has Better SG (team1, team2): ")
    if sg_comp == "team1":
        team1_ttl += 1 
    else:
        team2_ttl += 1 
   
    sf_comp = input("Who Has Better SF (team1, team2): ")
    if sf_comp == "team1":
        team1_ttl += 1 
    else:
        team2_ttl += 1 
    
    pf_comp = input("Who Has Better PF (team1, team2): ")
    if pf_comp == "team1":
        team1_ttl += 1 
    else:
        team2_ttl += 1 

    c_comp = input("Who Has Better C (team1, team2): ")
    if c_comp == "team1":
        team1_ttl += 1 
    else:
        team2_ttl += 1 

    print("Team1: " + team1_name + " " + str(team1_ttl) + " pts")
    print("Team2: " + team2_name + " " + str(team2_ttl) + " pts")

if __name__ == "__main__":
    main()
