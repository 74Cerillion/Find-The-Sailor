import bayes

results = []
iteration = 0

while iteration < 10000:

    app = bayes.Search("Cape Python")

    sailor_x, sailor_y = app.sailor_final_location(num_search_areas=3)

    sailor_found = False

    search_num = 1

    while not sailor_found:

        choices = {}

        if len(app.searched_a1) < 2500:
            choices[1] = app.p1
        if len(app.searched_a2) < 2500:
            choices[2] = app.p2
        if len(app.searched_a3) < 2500:
            choices[3] = app.p3

        choice = max(choices.keys(), key=choices.get)

        app.calc_search_effectiveness()

        if choice == 1:
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.actual_sep1)
            results_2, coords_2 = app.conduct_search(1, app.sa1, app.actual_sep1)
            app.actual_sep1 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.actual_sep2 = 0
            app.actual_sep3 = 0
        elif choice == 2:
            results_1, coords_1 = app.conduct_search(2, app.sa2, app.actual_sep2)
            results_2, coords_2 = app.conduct_search(2, app.sa2, app.actual_sep2)
            app.actual_sep1 = 0
            app.actual_sep2 = (len(set(coords_1 + coords_2))) / (len(app.sa2)**2)
            app.actual_sep3 = 0
        elif choice == 3:
            results_1, coords_1 = app.conduct_search(3, app.sa3, app.actual_sep3)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.actual_sep3)
            app.actual_sep1 = 0
            app.actual_sep2 = 0
            app.actual_sep3 = (len(set(coords_1 + coords_2))) / (len(app.sa3)**2)

        if results_1 == 'Not Found' and results_2 == 'Not Found':
            app.revise_target_probs()
            search_num += 1
        else:
            sailor_found = True

    iteration += 1
    print(iteration)
    results.append(search_num)

print(len(results))
total_turns = 0
for num in results:
    total_turns = total_turns + num
average_turns = total_turns / 10000
print(average_turns)