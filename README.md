# HashBeaf

You don't like your git commit hash `dc3fe60`?
Or any of your others hashes?
With HashBeaf you can easily create hashes with words that you like in it, such as `c0dec`, `abba` :musical_note:, `cafe` :coffee: or [`deadbeef`](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_debug_values) :cow:.
The last one is probably too long to work, so let's try `beaf` as hash instead (now you understand the name - not a typo :wink:).

The way this works is that it computes a commit time based on your previous commit to get the right hash, so do use it with care.


## Example

So you've made some changes to your git repository and staged some files.
Now, it is time to make a commit as normal:

```bash
$ git commit -m "Updated code"
[main b1c825b] Updated code
 12 files changed, 215 insertions(+), 2 deletions(-)
(...)
```
But before you push, you think, meh, `b1c825b`, I can do better than that.
Now it is time to run HashBeaf:
```bash
$ python src/hashbeaf.py c0de
[main c0de2c4] Updated code
 Date: Mon Jun 26 20:43:07 2023 +0200
(...)
```
And voila, we have `c0de2c4`, our HashBeaf'ed commit hash!


## Want to try it yourself?

Clone the repository, navigate to your own git repository, make a commit, and then run either:
```bash
python /path/to/hashbeaf/src/hashbeaf.py
```
to use a default list of nice 'words', or something like this for a custom 'word':
```
python /path/to/hashbeaf/src/hashbeaf.py c0de
```

If you think it is too much work to run this after each commit, you can also install a git post-commit hook for your repository.
Modify `post-commit` to point to the right absolute path (and customize it further as needed), and simple copy it to `your_repo/.git/hooks`.
On the next commit hashbeaf should run automatically.

Need some inspiration?
Check out the [default words list](src/words.py) for nice commit hashes, or see more on [Wikipedia here](https://en.wikipedia.org/wiki/Hexspeak) and [here](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_debug_values).


## Implementation details

The algorithm is inspired by [beautify_git_hash](https://github.com/vog/beautify_git_hash), a slightly outdated tool that achieves the same thing.

HashBeaf is implemented in Python and requires version 3.7 or newer.

HashBeaf works as follows.
A commit hash in git is computed based on the commit details, which include the commit message, author time and committer time.
If we modify any of those, we get a new commit hash.
With HashBeaf we set the author time and committer time to some time in the near future, compute a new hash, and if the hash starts with any of the user supplied 'words', we amend the previous commit by running something like:
```bash
GIT_COMMITTER_DATE=$(some_commit_time) git commit --amend -C HEAD --date=$(some_author_time)
```
HashBeaf keeps on changing the two times until either the given maximum time is reached or the nice hash is found.
The algorithm tries to found times as close as possible to the actual commit/author times.
For longer words (i.e. 5 characters or more) it is likely that the default maximum time is not enough: setting `--max_minutes_in_future` is recommended.
However, be careful with increasing the time: it might confuse other users of your repository or can lead to incorrectly sorted commits in logs.


## Feature wish list

Missing a feature?
Soon there will be also:

1. A pypi version that you can install as `pip install hashbeaf`.
2. More tests
3. More documentation
4. More error checking
