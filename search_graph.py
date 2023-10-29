import networkx as nx


def get_shortest_path_text(origin_string, destination_string):
    G = nx.Graph()  # Create a graph

    edge_labels = {
        1: "Cartoon Room",
        2: "Round Meeting Room",
        3: "3rd Floor Left Side Stairs",
        4: "3rd Floor Left Side Elevator",
        5: "3rd Floor Student Lounge",
        6: "BuckID Room",
        7: "3rd Floor Right Side Elevator",
        8: "3rd Floor Right Side Stairs",
        9: "Door Hallway",
        10: "2nd Floor Left Side Stairs",
        11: "2nd Floor Left Side Elevator",
        12: "2nd Floor Right Side Stairs",
        13: "2nd Floor Right Side Elevator",
        14: "2nd Floor Center Stairs",
        15: "Alumni Council Room",
        16: "SPHINX Room",
        17: "Senate Room",
        18: "Traditions Room",
        19: "Left Grand Ballroom Hallway",
        20: "Grand Ballroom",
        21: "Front Grand Ballroom Hallway",
        22: "2nd Floor Student Lounge",
        23: "Glass Lounge",
        24: "Leadership and Service Room",
        25: "1st Floor Left Side Stairs",
        26: "1st Floor Left Side Elevator",
        27: "1st Floor Right Side Stairs",
        28: "1st Floor Right Side Elevator",
        29: "1st Floor Center Stairs",
        30: "Espress-OH",
        31: "Union Market",
        32: "Woody's Tavern",
        33: "College Entrance",
        34: "Great Hall",
        35: "High Street Entrance",
        36: "Side Entrance",
        37: "Performance Hall",
        38: "Sloopy's Dinner",
        39: "1st Floor Lounge",
        40: "Lower Level Stairs",
        41: "Lower Level Elevator",
        42: "Basement Student Lounge"
    }

    source_to_start = {
        "basement_student_lounge": 42,
        "floor1_cafe_entrence": 33,
        "floor1_high_st_entrence": 35,
        "floor1_side_entrence": 36,
        "floor1_sloopys": 38,
        "floor2_alumni_room_in_corner": 15,
        "floor2_front_lounge": 22,
        "floor2_hallway_learship_service": 24,
        "floor2_main_ballroom": 20,
        "floor2_main_ballroom_front_hall": 21,
        "floor2_main_ballroom_left_hall": 19,
        "floor3_buckid": 6,
        "floor3_door_hall": 9
    }

    destination_to_end = {
        "Union Market": 31,
        "Great Ballroom": 20,
        "Sloopys Diner": 38,
        "Buckid Room": 6,
        "Espress OH": 30,
        "Woodys Tavern": 32,
        "West Entrance/Exit": 33,
        "East Entrance/Exit": 35,
    }

    use_stairs = True

    # 3rd Floor
    G.add_edge(1, 2, weight=40)
    G.add_edge(2, 3, weight=14)
    G.add_edge(3, 4, weight=18)
    G.add_edge(4, 5, weight=69)
    G.add_edge(5, 6, weight=46)
    G.add_edge(6, 7, weight=34)
    G.add_edge(7, 4, weight=27)
    G.add_edge(7, 8, weight=18)
    G.add_edge(8, 9, weight=1)

    # 3rd floor to 2nd floor
    if not use_stairs:
        G.add_edge(3, 10, weight=40)
        G.add_edge(8, 12, weight=40)
    G.add_edge(4, 11, weight=40)
    G.add_edge(7, 13, weight=40)

    # 2nd floor
    G.add_edge(15, 16, weight=24)
    G.add_edge(16, 17, weight=15)
    G.add_edge(17, 18, weight=16)
    G.add_edge(18, 19, weight=6)
    G.add_edge(19, 20, weight=7)
    G.add_edge(19, 11, weight=28)
    G.add_edge(10, 11, weight=13)
    G.add_edge(19, 11, weight=28)
    G.add_edge(20, 21, weight=12)
    G.add_edge(21, 22, weight=26)
    G.add_edge(21, 11, weight=30)
    G.add_edge(22, 13, weight=72)
    G.add_edge(23, 14, weight=8)
    G.add_edge(24, 12, weight=14)
    G.add_edge(12, 13, weight=17)
    G.add_edge(13, 14, weight=8)
    G.add_edge(14, 11, weight=20)
    G.add_edge(14, 10, weight=18)

    # 2nd floor to 1st floor
    if not use_stairs:
        G.add_edge(25, 10, weight=40)
        G.add_edge(27, 12, weight=40)
        G.add_edge(29, 14, weight=40)
    G.add_edge(11, 26, weight=40)
    G.add_edge(13, 28, weight=40)

    # 1st floor
    G.add_edge(30, 33, weight=8)
    G.add_edge(33, 31, weight=16)
    G.add_edge(31, 32, weight=4)
    G.add_edge(33, 25, weight=12)
    G.add_edge(25, 28, weight=13)
    G.add_edge(34, 26, weight=42)
    G.add_edge(34, 35, weight=24)
    G.add_edge(35, 36, weight=37)
    G.add_edge(35, 29, weight=45)
    G.add_edge(36, 37, weight=6)
    G.add_edge(36, 29, weight=13)
    G.add_edge(37, 28, weight=24)
    G.add_edge(27, 28, weight=18)
    G.add_edge(38, 27, weight=8)
    G.add_edge(39, 29, weight=27)
    G.add_edge(39, 25, weight=9)
    G.add_edge(39, 28, weight=14)

    # 1st floor to basement
    if not use_stairs:
        G.add_edge(29, 40, weight=40)
    G.add_edge(28, 41, weight=40)
    G.add_edge(7, 28, weight=79)

    # Basement
    G.add_edge(40, 41, weight=27)
    G.add_edge(40, 42, weight=15)

    destination = destination_to_end[destination_string]

    origin = source_to_start[origin_string]

    shortest_path = nx.shortest_path(G, source=origin, target=destination, weight='weight')
    print(shortest_path)

    G.add_edge(3, 10, weight=40)
    G.add_edge(8, 12, weight=40)
    G.add_edge(4, 11, weight=40)
    G.add_edge(7, 13, weight=40)
    G.add_edge(25, 10, weight=40)
    G.add_edge(27, 12, weight=40)
    G.add_edge(29, 14, weight=40)
    G.add_edge(11, 26, weight=40)
    G.add_edge(13, 28, weight=40)
    G.add_edge(29, 40, weight=40)
    G.add_edge(28, 41, weight=40)

    stupid_solution_to_my_problem = [[3, 10], [8, 12], [4, 11], [7, 13], [25, 10], [27, 12], [29, 14], [11, 26],
                                     [13, 28], [29, 40], [28, 41], [10, 3], [12, 8], [11, 4], [13, 7], [10, 25],
                                     [12, 27], [14, 29], [26, 11], [28, 13], [40, 29], [41, 28], [7, 28], [28, 7]]
    i = 0
    walk = 0
    ele_skips = 0
    # instruction_list = []
    info_string = f"You are currently at {edge_labels[shortest_path[i]]}"
    print(info_string)
    # instruction_list.append(info_string)
    for i in range(1, len(shortest_path)):
        if walk == -1:
            walk = 0
            continue
        current_loc = edge_labels[shortest_path[i]]
        if i != len(shortest_path) - 1 and any(
                x in [[shortest_path[i], shortest_path[i + 1]]] for x in stupid_solution_to_my_problem):
            next_loc = edge_labels[shortest_path[i + 1]]
            info_string += f"\n\n{i - ele_skips}. Take the {current_loc} to the {next_loc}."
            ele_skips += 1
            print(info_string)
            # instruction_list.append(info_string)
            walk = -1
        elif i == len(shortest_path) - 1:
            info_string += f"\n\n{i - ele_skips}. Continue forward until you reach your destination, {current_loc}"
            print(info_string)
            # instruction_list.append(info_string)
        elif walk == 0:
            info_string += f"\n\n{i - ele_skips}. Walk to {current_loc}"
            print(info_string)
            # instruction_list.append(info_string)
            walk += 1
        elif walk == 1:
            info_string += f"\n\n{i - ele_skips}. Continue past {current_loc}"
            print(info_string)
            # instruction_list.append(info_string)
            walk += 1
        elif walk == 2:
            info_string += f"\n\n{i - ele_skips}. Walk past {current_loc}"
            print(info_string)
            # instruction_list.append(info_string)
            walk = 1

    return info_string
