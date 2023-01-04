import re
from namematcher import NameMatcher

name_matcher = NameMatcher()


# Match score for two names:
score = name_matcher.match_names('This is fun and excitring', 'This is fun and excitring')
print(score)