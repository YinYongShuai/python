import numpy as np

lists = ['fnd17_oxlcxspebq', 'fnd17_shsoutbs','fnd17_oxlcxspebq', 'fnd28_value_05191q', 'fnd17_oxlcxspebq', 'fnd28_value_05192q','fnd17_oxlcxspebq', 'fnd28_value_05301q','fnd17_oxlcxspebq', 'fnd28_value_05302','fnd17_pehigh', 'fnd17_pelow','fnd17_priceavg150day', 'fnd17_priceavg200day','fnd17_priceavg150day', 'fnd17_priceavg50day','fnd17_priceavg200day', 'fnd17_priceavg50day','fnd17_pxedra', 'fnd17_tbea','fnd17_pxedra', 'fnd28_newa3_value_18191a','fnd17_pxedra', 'fnd28_newa3_value_18198a','fnd17_pxedra', 'fnd28_value_02300a','fnd17_pxedra', 'fnd28_value_05302','fnd17_pxedra', 'mdl175_ebitda','fnd17_pxedra', 'mdl175_pain']

new_list = np.unique(lists)

combinations = [(x, y) for x in new_list for y in new_list if x != y]

unique_combinations = set(tuple(sorted(combination)) for combination in combinations)

print("Total combinations:", unique_combinations.__len__())
for i in unique_combinations:
    alpha = "ts_regression(ts_zscore(" + i[0] + ", 500), ts_zscore(" + i[1] + ", 500), 500)"
    print(alpha)
    # ts_regression(ts_zscore(fnd17_oxlcxspebq, 500), ts_zscore(fnd17_shsoutbs, 500), 500)


