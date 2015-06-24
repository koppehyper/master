git config --global user.name 'koppehyper'
git config --global user.email 'koppehyper@gmail.com'

./hub pull-request -m 'Test PullRequest'
git checkout master
git merge --no-ff ${CIRCLE_BRANCH}
git push origin master
