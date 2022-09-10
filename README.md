# Conversation Assistant

Helping you find the right words.

I reckon I need some prefilled stuff on the frontend, such as the tone of the conversation. I'm not sure what I should do when all inputs are empty.

I should do a toLowerCase in the frontend when sending this stuff? Probs doesn't matter.

Dropdown options:
Relationship:

- Friend (default)
- Mother
- Father
- Girlfriend
- Boyfriend
- Partner
- Crush
- Wife
- Husband
- Enemy
- (custom)

Tone:

- Casual (default)
- Professional
- Flirty
- Serious
  (custom)

I can be described as:

- Funny
- Charming
- Mysterious
-

I want to be able to get good suggestions right off the bat, without filling out any details.

Add the ability to return multiple suggestions at once.

# What are my goal prompts?

## When all params given

The following is a conversation between Chad Johnson and Stacey, who is Chad Johnson's New match on a dating app.
I'm a 26 year old Software Dev who lives in Camberwell, Melbourne.
My pronouns are he/him.
My favourite hobbies include Chillin.
I can be described as A Bit Of A Wanker.
I want to sound Flirty.
In my spare time, I like to

Stacey: why yo ass so nasty 💩

Chad Johnson:

# baw
The following is a conversation between Lachie James and Gloria, who is Lachie James's crush.

<Lachie is about to say something awesome>

Gloria: Hey babe, how are you?
Lachie James: I'm good. Just thinking about you.
Gloria: Haha why?
Lachie James:  Because you're amazing and I can't stop thinking about you
Gloria: cringe
Lachie James:

# Damn a lot of these messages suck.  How do I make the prompts generate an awesome opening line?  I need to not sound so robotic in the input

Prompt stages:

Stage 1 - intro - my name, their name, this is a conversation
- my_name
- their_name
Stage 2 - extra - Add any extra properties that are passed
- age
- pronouns
- location
- hobbies
- self_description
Stage 3 - messages - add any previous messages
- previous_messages
Stage 4 - suggestion - add name
- my_name

If my_name or their_name is omitted, we should just omit both names for now.  We can get more detailed later.

We will have to use a different template that uses me/them

