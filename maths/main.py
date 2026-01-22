import numpy as np

if __name__ == '__main__':
    dataset = [18,21,37,46,57,48,53,52,68,22,30,33,35,19,20,40,41,52,57,46,48,53,52,68,22,30,33,35,36,66,70,57,27,38,39,44,59,51,61,69]
    sub_set_1 = np.random.choice(a=dataset,size=5,replace=True)
    sub_set_2 = np.random.choice(a=dataset,size=5,replace=True)
    mean_of_all_ages = np.mean(dataset)
    mean_of_subset_1 = np.mean(sub_set_1)
    mean_of_subset_2 = np.mean(sub_set_2)
    print(f"Person with max age: {np.argmax(dataset)}")
    print(f"Person with min age: {np.argmin(dataset)}")
    print(f"Mean of All Ages: {mean_of_all_ages}\nMean of Subset1 {mean_of_subset_1}\nMean of Subset2 {mean_of_subset_2}")
    print(np.random.choice(np.random.rand(1),size=5,replace=True))

