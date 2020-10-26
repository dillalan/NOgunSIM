from model import GunSIM


def run_model(policy_mugger, policy_victim, rep=365):
    sum_i = 0
    sum_ii = 0
    sum_iii = 0
    sum_iv = 0
    sum_homicide = 0
    sum_jailed = 0
    for i in range(rep):
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
    overall = sum_i + sum_ii + sum_iii + sum_iv
    print(f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
          f"I - {sum_i}; II - {sum_ii}; III - {sum_iii}; IV - {sum_iv}")
    print(
        f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
        f"I - {sum_i/overall}; II - {sum_ii/overall}; III - {sum_iii/overall}; IV - {sum_iv/overall}")
    print(f"Policy on Mugger:{policy_mugger}; Policy on Victim:{policy_victim} → "
          f"Homicides:{sum_homicide}; Arrests:{sum_jailed}")


if __name__ == '__main__':
    run_model(False, False)
    # print('\n')
    # run_model(True, True)
    # print('\n')
    # run_model(False, True)
    # print('\n')
    # run_model(True, False)
