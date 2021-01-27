def sorted_dict(x_dict, t_f):
    if t_f.xy[0] not in x_dict:
        x_dict.update({t_f.xy[0]: [t_f]})
    else:
        temps = x_dict[t_f.xy[0]]
        temps.append(t_f)
        # print(Hello)
    return x_dict
