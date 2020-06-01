Title: Discord Bot in .NET
Date: 2020
Category: Project
Tags: c#, json, bots, discord, mysql
Slug: discord-bot
Author: Thomas Brunbjerg
Summary: A Discord Bot developed in C# using the .NET Wrapper
featured_image: img/discord_bot_cover.gif
repository: https://github.com/ThomB93/DiscordBot

This bot was made using the unofficial .NET wrapper for the Discord API. More information about the wrapper can be found on the [Github repo](https://github.com/discord-net/Discord.Net)

In its simplest form, the bot makes use of the command service provided by the Discord Client to accept requests from users. All messages that match the specified prefix + alias will execute some function that the bot provides. As an example, here is a command that prints out a random trivia question to the user:

```c#
commands.CreateCommand("trivia")
    .Alias(new string[] { "question"}) 
    .Description("Provides a random question. !trivia [categoryId] [value]")
    .Parameter("categoryId", ParameterType.Required)
    .Parameter("value", ParameterType.Required) 
    .Do(async e =>
    {
        JsonQuestion question = new JsonQuestion(e.GetArg(0), Convert.ToInt32(e.GetArg(1)));
        DataContainer container = question.GetQuestions();
        int listLength = container.Questions.Count;
        Random r = new Random();
        int rand = r.Next(0, listLength); 
        await e.Channel.SendMessage(container.Questions[rand].question);

        discord.MessageReceived += async (s, f) => {
            if (f.Message.Text == container.Questions[rand].answer) 
                await f.Channel.SendMessage("Congratulations " + f.Message.User + "!");
        };
    });
```

The name of the command is 'trivia', while the alias is 'question'. For this bot, the prefix is set to the character '!'. In addition, the user can input some parameters to the command, such as a category ID and a value. When the users enters e.g. '!question Food 200' into the discord chat, the method will execute. A random question will be fetched and displayed and then the method hooks into the MessageReceived event handler, which is triggered whenever a user enter a message. A conditional statement checks whether the message was the correct answer to the question. If true, a message congratulating the user is shown. 
s
New command can be added in the same manner as shown above. The full documentation for the .NET wrapper can be found [here](https://docs.stillu.cc/guides/getting_started/first-bot.html).