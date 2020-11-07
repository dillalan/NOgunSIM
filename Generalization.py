from model import GunSIM
import plotly.graph_objects as go


def sankey_prep():
    start = {'Coop\n': 0, 'React\n': 0, 'Force\n': 0, 'nForce\n': 0}
    target = {'Coop\n': 0, 'React\n': 0, 'Force\n': 0, 'nForce\n': 0}
    c, r, f, nf = 0, 0, 0, 0
    kc, kr, kf, knf = 0, 0, 0, 0

    switch = {'Coop\n': 0, 'React\n': 0, 'Force\n': 0, 'nForce\n': 0}
    start_file = open('start.txt', 'r')
    target_file = open('target.txt', 'r')
    for i in target_file:
        if i != start_file.readline():
            switch[i] += 1
    start_file.close()
    target_file.close()
    start_file = open('start.txt', 'r')
    target_file = open('target.txt', 'r')
    for line in start_file:
        start[line] += 1
    for line in target_file:
        target[line] += 1
    resolution = open('step_mugging.txt', 'r')
    res=[]
    for line in resolution:
        res.append(int(line))
    # Number of initial strategy minus the ones that changed to the opposite strategy
    kr = start['React\n'] - switch['Coop\n']
    kc = start['Coop\n'] - switch['React\n']
    kf = start['Force\n'] - switch['nForce\n']
    knf = start['nForce\n'] - switch['Force\n']
    # Now placing all values that keep and changed strategy during the algorithm into a list
    value = [kr, switch['Coop\n'],
             kc, switch['React\n'],
             kf, switch['nForce\n'],
             knf, switch['Force\n'],
             res[0], res[1], res[2], res[3], res[0], res[3], res[1], res[2]]
    print(value)
    print(target)

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=40,
            line=dict(color="black", width=0.5),
            label=["React", "Coop", "Force", "nForce", "React", "Coop", "Force", "nForce",
                   "I - Fight", "II - Mugger Fail", "III - Voluntary Submission", "IV - Involuntary Submission"],
            color="blue"
        ),
        link=dict(
            source=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],  # indices correspond to labels, eg A1, A2, A2, B1, ...
            target=[4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 10, 11, 8, 11, 9, 10],
            value=value
        ))])
    fig.update_layout(title_text="GunSIM for classic Mugging Game(BRAMS, 1993)", font_size=10)
    fig.show()


def save_data(i, ii, iii, iv):
    with open('step_mugging.txt', 'w') as f:
        f.write(f'{i}\n')
        f.write(f'{ii}\n')
        f.write(f'{iii}\n')
        f.write(f'{iv}\n')


def run_model(policy_mugger, policy_victim, years=1):
    sum_i = 0
    sum_ii = 0
    sum_iii = 0
    sum_iv = 0
    sum_homicide = 0
    sum_jailed = 0
    sum_guns = 0
    overall = 0
    for i in range(years):
        for days in range(365):
            sim = GunSIM(policy_mugger=policy_mugger, policy_victim=policy_victim)
            sim.grow_victims()
            sim.grow_robbers()
            sim.step()
            sum_i += sim.return_counter()[0]
            sum_ii += sim.return_counter()[1]
            sum_iii += sim.return_counter()[2]
            sum_iv += sim.return_counter()[3]
            sum_homicide += sim.return_counter()[4]
            sum_jailed += sim.return_counter()[5]
            sum_guns += sim.return_counter()[6]
        overall = sum_i + sum_ii + sum_iii + sum_iv
    save_data(sum_i, sum_ii, sum_iii, sum_iv)
    print(f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
          f"I - {sum_i / years}; II - {sum_ii / years}; III - {sum_iii / years}; IV - {sum_iv / years}")
    print(
        f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
        f"I - {sum_i / overall}; II - {sum_ii / overall}; III - {sum_iii / overall}; IV - {sum_iv / overall}")
    print(f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
          f"Homicides:{sum_homicide / years}; Arrests:{sum_jailed / years}; Active Guns:{sum_guns / years}")
    sankey_prep()


if __name__ == '__main__':
    #sankey_prep()
    run_model(False, False)
    # print('\n')
    #run_model(True, True)
    # print('\n')
    # run_model(False, True)
    # print('\n')
    # run_model(True, False)
