# 1) Current Team Tier Level 'Tier 1 = 5pts', 'T2 = 3pts', 'T3 = 1pts'
# 2) Past 4 Games played; T1 Win = 5, T2 = 3, T3 - 1, 
#   a) Add 2pts for T1 Away Win, or 1pts for T2 Away Win, no added for T3
# 3) Compare team starters 1pt for each better player
# 4) Current Home Team gets 3pts

def main():
    team1_ttl = 0
    team2_ttl = 0

    team1_name = input("Enter Team 1: ")
    tm_lvl = int(input("Enter Team Level (1,2,3): "))
    team1_ttl += (tm_lvl**1.5)
    current_gm_home = input("Home Team in Comparison (binary): ")
    if current_gm_home == '1':
        team1_ttl += 2
    else:
        team2_ttl += 2
    n = 1
    while n < 5:
        w = int(input("Is Game "+str(n)+" a Win (binary): "))
        if w == 0:
            n+=1
            continue
        l = int(input("What was the Opp Tm Lvl (worst 1,2,3 best): "))
        if l == 1:
            n+=1
            continue
        a = int(input("Is Game "+str(n)+" an away game (binary): "))
        team1_ttl += (w*(l**1.5 + 2*a))
        n += 1
    x = int(input("What is the X-Factor Score: "))
    team1_ttl += x

    team2_name = input("Enter Team 1: ")
    tm_lvl = int(input("Enter Team Level (1,2,3): "))
    team2_ttl += (tm_lvl**1.5)
    n = 1
    while n < 5:
        w = int(input("Is Game "+str(n)+" a Win (binary): "))
        if w == 0:
            n+=1
            continue
        l = int(input("What was the Opp Tm Lvl (worst 1,2,3 best): "))
        if l == 1:
            n+=1
            continue
        a = int(input("Is Game "+str(n)+" an away game (binary): "))
        team2_ttl += (w*(l**1.5 + 2*a))
        n += 1
    x = int(input("What is the X-Factor Score: "))
    team2_ttl += x


    if team1_ttl == team2_ttl:
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
