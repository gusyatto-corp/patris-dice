# Patrisが100面ダイスとか振ってくれるみたいなのですが

## About

DiscordでTRPGのダイスロールをしてくれるBot。

## Usage

### Basic Usage

ボットがJoinしているサーバーのチャンネルで、以下のような書式のメッセージを送ると、
ダイスロールの結果をリプライしてくれます。
```
[number<10]["d" or "D"][number>0]
```

例えば、

```
1d100
```

と送信すると

```
@you
res: [6]-> 6
```

と返してくれます。

### Diceroll with Note

メモつきでダイスロールをするためには、以下のようにします。

```
[number<10]["d" or "D"][number>0] [message]
```

例えば、

```
1d100 sanc
```

と送ると、

```
@you
Dice rolled for "sanc"
res: [4]-> 4
```

と返してくれます。

### Secret Diceroll

ダイス書式の後ろに「シークレット」と入れると、
個人チャットにシークレットダイスロールの結果を送信します。

例えば、

```
1d100 シークレット 心理学
```

と送ると、

```
@you
Dice rolled for "心理学"
res: [96]-> 96
```

と個人チャットに送信されます。

## Environment

- Windows 10
- Python 3.6

## Contact

何か不具合があったり、機能のリクエストがあればこちらにご連絡ください。

`twitter`: `@ninisan_drumath`