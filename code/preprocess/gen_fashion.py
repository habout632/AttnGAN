import os
import pickle
import random
from shutil import copy2

fashion_dir = "/data2/fashion"


def construct_images():
    """
    """

    images_dir = os.path.join(fashion_dir, "images")
    vton = os.path.join(fashion_dir, "cp-vton")
    fashions = os.listdir(vton)
    for fashion in fashions:
        sub_dir = fashion.replace(".jpg", "")
        dir = "{}/{}".format(sub_dir, fashion)
        print(fashion)
        os.mkdir(os.path.join(images_dir, sub_dir))
        copy2(os.path.join(vton, fashion), os.path.join(images_dir, dir))


def construct_texts():
    """

    :return:
    """
    texts_dir = os.path.join(fashion_dir, "text")
    with open(os.path.join(fashion_dir, "descriptions.txt"), "r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(" ")
            filename = words[0]
            print(filename)

            sub_dir = filename.replace(".jpg", "")
            # mkdir
            sub_path = os.path.join(texts_dir, sub_dir)
            if not os.path.exists(sub_path):
                os.mkdir(sub_path)

            # test
            text_file = filename.replace(".jpg", ".txt")
            # if not os.path.isfile(os.path.join(sub_path, text_file)):
            with open(os.path.join(sub_path, text_file), "w") as h:
                h.write(" ".join(words[1:]))


def split_train_test():
    """
    train:test = 7:3
    :return:
    """
    vton = os.path.join(fashion_dir, "cp-vton")
    fashions = os.listdir(vton)
    print(fashions)
    print(["{}/{}".format(fashion.replace(".jpg", ""), fashion.replace(".jpg", "")) for fashion in fashions])
    fashions = ["{}/{}".format(fashion.replace(".jpg", ""), fashion.replace(".jpg", "")) for fashion in fashions]
    random.shuffle(fashions)
    print(len(fashions))
    split = int(len(fashions) * 0.7)
    train = fashions[:split]
    test = fashions[split:]
    print(train)
    print(test)

    filename = "filenames.pickle"
    train_dir = os.path.join(fashion_dir, "train")
    with open(os.path.join(train_dir, filename), "wb") as f:
        pickle.dump(train, f)

    test_dir = os.path.join(fashion_dir, "test")
    with open(os.path.join(test_dir, filename), "wb") as f:
        pickle.dump(test, f)
    return


if __name__ == "__main__":
    split_train_test()
