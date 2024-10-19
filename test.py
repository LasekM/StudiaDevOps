''' @LasekM ➜ /workspaces/StudiaDevOps (main) $ git checkout -b dev
Switched to a new branch 'dev'
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py

nothing added to commit but untracked files present (use "git add" to track)
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git add .
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   main.py

@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git commit -m "Add new file, main.py"
[dev 90cf4f7] Add new file, main.py
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log
commit 90cf4f73e70ccc9d2d165b148eac639c7ef07ada (HEAD -> dev)
Author: Mateusz Lasek <poltok00@gmail.com>
Date:   Sat Oct 19 13:42:20 2024 +0000

    Add new file, main.py

commit 9607898d0bc6de7836667e54a9d04a4f291cad87 (origin/main, origin/HEAD, main)
Author: Mateusz Lasek <poltok00@gmail.com>
Date:   Sat Oct 19 15:02:49 2024 +0200

    Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log --oneline --graph --all
* 90cf4f7 (HEAD -> dev) Add new file, main.py
* 9607898 (origin/main, origin/HEAD, main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git push origin dev
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 299 bytes | 299.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/LasekM/StudiaDevOps/pull/new/dev
remote: 
To https://github.com/LasekM/StudiaDevOps
 * [new branch]      dev -> dev
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git add .
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log --oneline --graph --all
* 90cf4f7 (HEAD -> dev, origin/dev) Add new file, main.py
* 9607898 (origin/main, origin/HEAD, main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git commit -m "Add test.py"
[dev 159082f] Add test.py
 1 file changed, 1 insertion(+)
 create mode 100644 test.py
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git push origin dev
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 329 bytes | 329.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/LasekM/StudiaDevOps
   90cf4f7..159082f  dev -> dev
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git push origin dev
Everything up-to-date
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log --oneline --graph --all
* 159082f (HEAD -> dev, origin/dev) Add test.py
* 90cf4f7 Add new file, main.py
* 9607898 (origin/main, origin/HEAD, main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git status
On branch dev
nothing to commit, working tree clean
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log --oneline --graph --all
* 159082f (HEAD -> dev, origin/dev) Add test.py
* 90cf4f7 Add new file, main.py
* 9607898 (origin/main, origin/HEAD, main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git push origin dev
Everything up-to-date
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ gst
bash: gst: command not found
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git status
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.py

no changes added to commit (use "git add" and/or "git commit -a")
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git add test.py 
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git commit -m 'TEST'
[dev ab10e48] TEST
 1 file changed, 3 insertions(+), 1 deletion(-)
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git push origin dev
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 283 bytes | 283.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/LasekM/StudiaDevOps
   159082f..ab10e48  dev -> dev
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git logs ^C
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git log --oneline --graph --all
* ab10e48 (HEAD -> dev, origin/dev) TEST
* 159082f Add test.py
* 90cf4f7 Add new file, main.py
* 9607898 (origin/main, origin/HEAD, main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (dev) $ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git fetch --all
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
Unpacking objects: 100% (3/3), 285 bytes | 285.00 KiB/s, done.
remote: Total 3 (delta 0), reused 2 (delta 0), pack-reused 0 (from 0)
From https://github.com/LasekM/StudiaDevOps
   9607898..948e854  main       -> origin/main
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git log --oneline --graph --all
* ab10e48 (origin/dev, dev) TEST
* 159082f Add test.py
* 90cf4f7 Add new file, main.py
| * 948e854 (origin/main, origin/HEAD) Add new file, main.py
|/  
* 9607898 (HEAD -> main) Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git reset --hard origin origin/main
fatal: Cannot do hard reset with paths.
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git reset --hard \origin/main
HEAD is now at 948e854 Add new file, main.py
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git reset --hard origin/main
HEAD is now at 948e854 Add new file, main.py
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git log --oneline --graph --all
* ab10e48 (origin/dev, dev) TEST
* 159082f Add test.py
* 90cf4f7 Add new file, main.py
| * 948e854 (HEAD -> main, origin/main, origin/HEAD) Add new file, main.py
|/  
* 9607898 Initial commit
@LasekM ➜ /workspaces/StudiaDevOps (main) $ git checkout -b dev1
Switched to a new branch 'dev1'
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ git add .
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ git commit -m "Test"
[dev1 ad68a5d] Test
 1 file changed, 1 insertion(+)
 create mode 100644 test.py
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ git push^C
(failed reverse-i-search)`gitr origin/mainorigin/main': ^Ct commit -m "Test"
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ ^C
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ ^C
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ git push origin dev1
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 310 bytes | 310.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'dev1' on GitHub by visiting:
remote:      https://github.com/LasekM/StudiaDevOps/pull/new/dev1
remote: 
To https://github.com/LasekM/StudiaDevOps
 * [new branch]      dev1 -> dev1
@LasekM ➜ /workspaces/StudiaDevOps (dev1) $ '''