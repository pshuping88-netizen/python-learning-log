#Structured Calc & Output
#Player Score system:
players_data = [{"Name":"TheNicky13","Kills":12,"Assists":4},{"Name":"22wyd","Kills":7,"Assists":5},{"Name":"Shawn123","Kills":3,"Assists":3}]

for player in players_data:
    total_contribution = player["Kills"] + player["Assists"]
    print(player["Name"])
    print(f"Total Contribution(Kills+Assists): {total_contribution}")

#Workout Tracker:
workout_data = [{"Name":"Squats","Sets":7,"Reps":9},{"Name":"Pushups","Sets":5,"Reps":12},{"Name":"Situps","Sets":11,"Reps":4}]

#intializing
highest_excercise = 0
total_workout_reps = 0

for excercise in workout_data:
    total_reps = excercise["Sets"] * excercise["Reps"]
    total_workout_reps = total_workout_reps + total_reps
    
    if total_reps > highest_excercise:
        highest_excercise = total_reps
        excercise_name = excercise["Name"]

print(f"Total reps: {total_reps}\n Total workout reps: {total_workout_reps}\n Excercise with highest reps: {excercise_name}\n Highest Reps: {highest_excercise}")

#Movie Rating Report (Main Drill)
movie_data = [{"Title":"War Machine","Rating(out of 10)":6,"Watch Count":786},{"Title":"Until Dawn","Rating(out of 10)":5,"Watch Count":685},{"Title":"People We Meet On Vacation","Rating(out of 10)":7,"Watch Count":898}]

#initializing
highest_engagement = 0
overall_engagement = 0

#Structured Output on Calculated Data
print(f"\n----- MOVIE REPORT -----")

for movie in movie_data:
    total_engagement = movie["Rating(out of 10)"] * movie["Watch Count"]
    overall_engagement = overall_engagement + total_engagement
    if total_engagement > highest_engagement:
        highest_engagement = total_engagement
        highest_movie = movie["Title"]
    print(f"\n{movie['Title']} Score: {total_engagement}")

print(f"\n----------\nTotal Engagement: {overall_engagement}\nTop Movie: {highest_movie}")

#Subscription Tracker
subscription_data = [{"Name":"Spotify","Monthly Cost":49.50,"Months Used":4},{"Name":"Netflix","Monthly Cost":229.99,"Months Used":7},{"Name":"Microsoft 365","Monthly Cost":159.59,"Months Used":6}]

#Structured Output on Calculated Data
print("\n----- SUBSCRIPTION REPORT -----\n")

#intializing & threshold
total_spending = 0
threshold = 200

for sub in subscription_data:
    total_spent = sub["Monthly Cost"] * sub["Months Used"]
    total_spending = total_spending + total_spent
    if total_spent > threshold:
        print(f"{sub['Name']} Total Spent: {total_spent}\n")
        
print(f"----------\nTotal Spend: {total_spending}")