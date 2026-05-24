## Research: GenAI is built on consensus

Before getting to our decision framework, we need to understand what GenAI is and is not. When encountering something new, it’s common for humans to try to draw analogies and extrapolations based on existing technologies, which may be counterproductive in building an understanding based on first principles.

  

We will discuss the evolution from training a machine learning model to training a large language model in the bonus module. Here we summarized the key insights from that module. So we can assess which tasks we shall give to GenAI.

**GenAI is good at dealing with consensus in the training data** because the way it is trained – assigning probability of the next token based on a huge amount of training text. So the more a particular piece of knowledge appears in the training data – mostly text from the internet – the better GPT is about recalling it, and using it. So GPT is good at programming partially because code is structured and predictable, and partially because there is a lot of code as training data fed into GPT. But for less common programming languages, e.g. Rust, GPT is more likely to make mistakes.

**For less common facts, GenAI hallucinates**, i.e. confidently says something wrong. This is rooted in the underlying mechanism, next token prediction. The model always gives the answer that it is most confident with. To the model, there is no way of knowing the difference between a right answer vs. a wrong answer. In other words, whether a fact is true is never an explicit goal to optimize during training. The correctness is only ensured by the consensus. If it appears often, GenAI will get it right. If not, GenAI just hallucinates.

Hallucination can be controlled by walkarounds outside of the model. For example, New Bing (Copilot) uses search engines to tell the model to construct its answers around the search results. Providing a document as context and constraining the responses of GenAI based on the docs, can also help.

  
**For less common tasks, GenAI says something correct but useless.** For example, nothing prevents us from asking GPT how to get rich. It will provide seemingly helpful suggestions. They are correct, but mostly useless. This is again because GPT is trained to output the consensus of the training data. If we expect GPT outputs an email draft that reads smooth and natural, that's a reasonable expectation. Because it's the average level of the books and Internet posts. But if we expect GPT to write an effective marketing email that can make money for us, that's not reasonable. Because this is exceptional content. Emails that can make money are probably among the top 1% of the Internet in terms of quality, rather than the majority or the average.

## Conjecture: How is GenAI different from humans?

Our understanding of brain science and neuroscience is limited, so we can only seek answers from philosophy. By the way, unless there is a major paradigm shift in brain science, brain-computer interfaces like Neuralink are unlikely to achieve the functionalities people imagine. But we are not philosophy experts, so take this as a reference.
### **Judgment**
No matter how capable ChatGPT is, it can only absorb digital signals and cannot interact with the real world. It might learn from ten thousand experts that doing A leads to B, but without experimenting in the real world, it can't verify from the ground up whether this is true or false. True understanding of such matters requires personal experience.
### **"Eureka"**
Newton saw an apple fall and discovered gravity, predicting the motion of the stars. Before Copernicus, everyone saw the sun rise and set and believed it revolved around the Earth. If ChatGPT existed then, it would surely assert that the sun revolves around the Earth. While it might predict how a peach falls from how an apple falls, it's unlikely to deduce the motion of the stars.

However, people who discover things like gravity are rare. More importantly, it's about identifying what this cognitive ability is and how it manifests in our daily lives. Archimedes shouted "Eureka" when he discovered the principle of buoyancy while bathing, describing moments of "sudden inspiration and insight." This moment can be specifically described as "connecting several related points and discovering a third."

This is actually two steps: the first is to discover new knowledge, and the second is to immediately understand its importance. ChatGPT may discover many things, including the principle of buoyancy (I'm not sure). But ChatGPT cannot know the importance of this knowledge or whether it's useful to people. This step definitely requires human input.
### **Critical Thinking**
Critical thinking involves actively distinguishing truth from falsehood, continually discovering more important, more realistic, and more creative and valuable ideas. ChatGPT might find a good answer, but whether it can continually challenge and improve upon that answer is uncertain. It's a capability that OpenAI should continue to explore and develop.
### **Understanding Humans**
Human textual knowledge certainly contains much understanding of human nature, but there are also aspects of human nature or preferences that are not documented in text. Combining this with a real-world understanding of people, rather than through surveys or online data, brings an incremental understanding that is a human advantage over ChatGPT.
### **Intuition**
Returning to the essence of ARLLM. ARLLM tries to generate the next word, but whether humans are doing this is unclear. If it's about generating the next sentence or paragraph, then perhaps the human advantage lies in generating the idea that comes much later. This might be what is called a "digital definition" of intuition. It's uncertain whether the model can achieve this, but it's likely difficult.
### **Interaction with the physical world**
Despite wishful thinking or extrapolations, Robotics is still a challenging problem, and there is no evidence of a “GPT” moment for Robotics. GPT may accelerate the development of Robotics gradually, but it will take a long time to pick up the speed. Until we see clear evidence, we should assume that Robots are bad at achieving human tasks of interacting with the world, and the development is still slow.

## Takeaway 1: Work with hallucination

This conclusion is not a research finding, but our conjectures based on our understanding of the research. Take it with a grain of salt.

**Hallucination is fundamental to large language models** because the underlying mechanism is next token prediction. All the results are the highest probability outcomes of large language models. In other words, the model always gives the answer that it is most confident with. To the model, there is no way of knowing the difference between a right answer vs. a wrong answer.

  

![](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCUHNEU1FNPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--5602bb0399599ce74aac6b3664dd861d344c8840/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJNEJEQTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--7535ef66ff04b52d1ea165e904a77a64f9cc7389/image.png)

**Hallucination is inevitable for useful GenAI systems** because the world is not deterministic. Truism is useless. In fact, this module is an example – in our attempt to provide useful predictions and conclusions, we have to step outside of being correct all the time.

  

Even with traditional ML systems, we have to allow models to explore, or it will get stuck in a saddle point (local optima) very quickly. For GenAI models, we have to allow flexibility, and given its nature of next token prediction, this inevitably creates hallucination.

  

**Hallucination can be controlled by walkarounds** outside of the model. For example, New Bing uses search engines to fact check and tell the model to construct its answers around the search engine results. Providing a document as context and constraining the responses of GenAI based on the docs, can also help.

  

**Software is exact input, exact output, while GenAI is fuzzy input, fuzzy output. GenAI has great potential but the ecosystem is not ready yet.** Every time we prompt GPT, it can give a different answer, but meanwhile, we can use multiple different ways of prompting GPT to complete the same task. This fuzzy input and fuzzy output is fundamentally different from old softwares. 

  

In the short term to mid term, the most effective way of using GenAI is to merge with the existing ecosystem, which is what we teach here. However, I hope we keep attention on this fuzzy input, fuzzy output nature of GenAI. In the long run, when the ecosystem is evolving towards this pattern, big opportunities may emerge from here, because this pattern allows us to achieve something completely new.

## Actionable guildline: Which tasks shall I delegate to GenAI?

The bad thing is, GenAI cannot and will not solve all our problems. But the good thing is, it means we humans, as a whole, are still irreplaceable. However, individual jobs will get replaced, and other jobs will emerge. The invention of engines did not just turn coachman to drivers, but unlocked the capacity of lifting tons of cargo across land, and made modern civilization possible. Almost everything we consume today is related to engines.

Therefore, for a fundamentally disruptive technology like GenAI, we shouldn’t be too zoomed in and should take a developing perspective. Otherwise, if you are focused on the most seemingly shortcomes of GenAI (short context window, limited integration with existing tools), after the development of the next generation of GPT that is much more capable, or after the ecosystem becomes more mature, your work can be irrelevant soon. 

Our framework ignores what GenAI is temporarily bad at and focus on the fundamental limitation of GenAI.

  

## **Is it a consensus?**

  

That immediately translates to an actionable guideline on which task to delegate to GenAI: ask yourself, "is consensus what I want?" If the answer is yes, use GenAI. If not, use your own brain to decompose the problem, and delegate subproblems that accept consensus to GenAI.

  

Let's take a look at a few examples.

- Summarizing a given material: this is a task that appears often online. So OK to delegate to GenAI.
    
- Learn about basic facts about seafood: that's a good task to delegate to GenAI. Because these are common materials that have good coverage on the Internet.
    
- Learn about research level knowledge on a specialized species of fish: this is not the consensus or majority of the Internet. So GenAI is likely to hallucinate. The solution is to first search online, and then ask GenAI to summarize the results. 
    
- Tasks that require creativity or insights: this by definition is not consensus. So we'd better rely on our brain and delegate automatable tasks to GenAI.
    

  

## **Is it a transformation task?**

  

There is one specific category of tasks that GenAI is especially good at: **the “transformation” tasks**, such as

- Translating natural languages – English to French
    
- Transform your idea from natural language to a programming language (AI-assisted programming)
    
- Transform from a lengthy article to a brief style (summarization)
    
- Transform a precise and scientific description to an easy-to-digest style (explain quantum physics to a six-year-old)
    

  

As long as we have a specific description of the target language, GenAI will do the job well. It even applies to some very specific cases. Think about the JIRA API example we showed at the beginning of the course. Essentially, what happened is we invented a language with only three words, one for each Jira API, and then we asked the GenAI to translate our natural language to that language, and it did the job really well.

After all, large language models are fundamentally transformers.

We've talked a lot about where and how to use AI, and after the two weeks' time, many people must have gotten used to AI and now possess a mindset of asking, "Shall I build something to solve this issue?" to the project they face. This is great, and I'm sure you gradually find out the benefit, but one warning is, it's actually a time when another common pitfall appears, that is overusing AI to do everything. 

  

## **Is it a factual task or a reasoning task?**

  

Compared to traditional ways – Google, Wiki, or even Siri – GenAI is way better at reasoning tasks, but due to its hallucination, does not do factual tasks well.

Factual tasks are those that require the AI to have an accurate memory of some knowledge or facts. For example, what city is the capital of the US? And reasoning tasks rely more on reasoning capabilities, on the given information. For example, given the following 10 lines of text, only keep the ones that are relevant to geography. 

  

Note, this is not a very scientific or rigorous division. Many or actually most tasks require the AI to have both knowledge and reasoning or deduction capabilities. But only some of them heavily depend on accurate recall of knowledge. For example, we are not sure about whether SQL uses = or == to indicate equivalence. So we ask AI. And to get this right, AI is expected to recall exactly from its knowledge. This is a factual task. For the task of summarizing given texts, it does require some knowledge of how to effectively summarize something. But the key to accomplishing this task doesn't lie in a precise recall of some facts. So it's a reasoning task. 

  

## **Is it a repetitive task or a creative task?**

  

A common misconception is to consider “design” as a creative task, when in fact, most “design” jobs are repetitive – they fulfill a certain customer demand, using templates or follow a certain workflow. The requirement of the job is not to express your art, or to be innovative, but to complete the task efficiently with low cost.

  

So think hard on what “creative” means – innovative, original, think outside of the box, connecting the dots, intuitive, and so on. It requires you to create a new solution, and as we explained before, such a solution won’t be thought of by GenAI.

  

Most work is a blend of repetitive tasks and creative tasks. Our case of WBR from Module 2 is a good example. There are certain parts of WBR – the things that we automated – are repetitive, but drawing insights from the data, is creative. Use GenAI for the repetitive tasks and focus your attention, effort, and time on creative tasks. You will be rewarded.

  

## **Pitfall: Respect and Develop Your Core Competency**

  

I (Yan here) want to share a true story here. After a few weeks of extensive use of AI, I felt I'm a power user now, and a big advocate of doing everything using AI. Instead of striking the keyboard, I dictate to the phone when writing, for writing, so the AI first does speech recognition, and then paraphrases the core points in an organized way. I draft emails using ChatGPT. I also write programs using ChatGPT, of course, and then I gradually fall into a weird state without knowing it. Yuzhen first found my writing is degrading; it smells like AI. More importantly, it becomes harder to understand than before because I was using some sophisticated but hard-to-understand words. My wife is complaining that my emails, and the emails I probably drafted for her using AI, read weird. "Put away your AI, and I will write my own emails." "The thing it wrote just doesn't sound like humans," she said. And when I took another look at the code I wrote on my hobby projects, it appeared in high quality with great comments and doc strings, but it lacks extensibility and maintainability from a professional perspective.

So I suddenly realized, I like using AI because it makes me feel good. I can also write articles or emails with sophisticated words even as a non-native speaker. I can easily write programs with strict adherence to the standard practice of comments and variable naming. I'm doing things well and easy. Everything appears fine, only gets better. 

But it's actually deceiving. My writing is actually harder to understand and didn't serve the purpose of communication. My coding is also worse because it's harder to maintain. What's especially bad is I lost the ability to discover this by myself. Because I am used to the life of asking AI to do the heavy lifting and copy-pasting the results. I am not familiar with thinking anymore. This makes me distracted by the appearance AI provides. Sophisticated words, beautiful comments. And this gradually dragged my attention from the things that really matter. Affection in the text, quality of the code. What's worse is this distraction further lowered my bar and made me gradually get used to delegating the tests that AI isn't good at to it and got okay on the low-quality results without knowing it. That's actually why I become an advocate of AI and delegate everything to it happily because I lost the key ability of assessing the quality. 

  

That's why I did a thorough reflection and tried to share what I learned here. Defining the success criteria beforehand. Assessing AI's results all the time. If we must fail, fail fast instead of accepting a low-quality result and claiming a victory. If you follow these practices, you're unlikely to fall into the same pitfalls I fell into.

But there is still one extra thing I wanted to share. That is, we need to always be clear about what our core value is in the role in our job and never delegate it to AI. There are two reasons. On one hand, if AI can do your core job well, you probably would want to learn something new and change your job. So it's reasonable to assume AI cannot do your core job well, which is still fortunately true because in most cases, that will require critical thinking and insights, which the current AI still lacks. On the other hand, as shown in my example, it's actually easier to get lost in the ease of using AI, and this loss will often impact (although not completely remove) your capabilities of thinking and doing the job. We don't want to risk that. 

  

Therefore, nowadays, I still delegate email writing to AI for unimportant emails. But when I need to make some point or impact someone, I will still strike the keyboard or use my fountain pen. But that doesn't mean AI is not useful anymore. I still use speech recognition to accelerate typing and GPT to correct any grammar mistakes. And it's still much more efficient than myself in the pre-AI era.

## Takeaway 2: Valuable opinions are contrarian, which GenAI cannot offer

There are lots of tasks in our work that seem impactful, but true impact comes from making progress, and progress usually requires holding a contrarian view and being correct. The reason is simple – if an opportunity is a consensus, it’s probably been taken already. 

  

Some examples of valuable work

- Invented a simplified method to complete a previously complex task – contrarian view on which methods are necessary
    
- Achieved something that other people deem impossible – contrarian view on the vision
    
- Killed a wasteful project – contrarian view on value
    
- Applied the business to a new domain – contrarian view on opportunities
    

That’s why when you ask GPT generic questions like “how do I get rich” or “how to make my products better”, GPT can give you a lot of seemingly useful analysis, but not any actual useful idea. The core of this problem is that the answer to your question doesn’t exist in the collective knowledge of the Internet, which GPT is trained on. Or, even if it does exist, but is not the most common result, GPT won’t assign a high probability to it, and won’t show it as its default answer.

That’s good. That means we are irreplaceable, if we can be contrarian and correct. Hope our course can help you get there. The formula is simple – 

- Delegate the repetitive, tedious, non creative jobs to GenAI as much as possible
    
- Develop your contrarian view and build it
    
- Learn through building