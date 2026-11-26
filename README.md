# describe-your-ex-in-one-word

[![make.fun · u-puan-describe-your-ex-in-one-word-9fc6ebe7](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/museweilejing923/describe-your-ex-in-one-word/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/museweilejing923/describe-your-ex-in-one-word/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)

The entry:

> expired

7 characters, limit 111.

One word, one verdict, no second chances. It reads like a label on a carton in the back of the fridge: short, final, and past its date. The relationship has passed its date and there is nothing left to salvage, and the word says all of that without a caption, an excuse, or a punctuation trick. In a head-to-head vote the word has to read instantly as a judgement on a former partner.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed word through a table of named rules and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The rules, in table order, are: no punctuation, no initial capital letter, non-empty, within the 111-character limit, exactly one word, contains letters, no control characters, no leading or trailing space, not digits only, and no double spaces or newlines.
