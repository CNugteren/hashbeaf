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

Clone the repository and run the above command.

Missing a feature?
Soon there will be also:

1. A pypi version that you can install as `pip install hashbeaf`.
2. A pre-commit hook
3. More tests
4. A list of nice words
5. More documentation
6. More error checking
