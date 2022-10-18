import git
from git import Repo
import os

root_folder = "C:/Users/EMMANUEL/Desktop/100 Days"
#
repos = Repo.init(root_folder)
repos.description = "100 Days of Code"
repo_name = repos.description
repository = git.Repo(root_folder)

for folder in os.listdir(root_folder):
    print(folder)
    if 'Day' in folder.split('-'):
        day_num = folder.split('-')[1]
        commit_message = f"Added Day {day_num}"
        print(commit_message)

        folder_path = root_folder + f"/{folder}"
        print(folder_path)
        # Add the folder to the repository
        repos.index.add(folder)
        repos.index.commit(message=commit_message)

    else:
        print(folder)
#
# origin = repos.create_remote("origin", 'https://github.com/RhythmBear/100DaysTest.git')
#
# assert origin.exists()
# assert origin == repos.remotes.origin == repos.remotes["origin"]
# origin.fetch()  # assure we actually have data. fetch() returns useful information
# #
# # repos.create_head("master", origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
#
# origin.push()  # attempt push, ignore errors
# origin.push().raise_if_error()  # push and raise error if it fails
# # assert not empty_repo.delete_remote(origin).exists()     # create and delete remotes
