import random
import re
from PyQt5 import QtWidgets, QtGui, QtCore

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Social Work GPT")
        self.setGeometry(100, 100, 400, 500)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.title_label = QtWidgets.QLabel("Social Work GPT", self)
        self.title_label.setFont(QtGui.QFont("Helvetica", 16, QtGui.QFont.Bold))
        layout.addWidget(self.title_label)

        self.conversation_text = QtWidgets.QTextEdit(self)
        self.conversation_text.setReadOnly(True)
        layout.addWidget(self.conversation_text)

        self.user_input_entry = QtWidgets.QLineEdit(self)
        self.user_input_entry.setFixedWidth(250)
        layout.addWidget(self.user_input_entry)

        self.user_input_entry.setPlaceholderText("Type in a message")
        self.user_input_entry.mousePressEvent = self.clear_placeholder

        self.user_input_entry.returnPressed.connect(self.handle_user_input)

        self.rules = [
            {
        "patterns": [r".*(feeling down|feeling sad|depressed|sad).*"],
        "responses": [
            "I'm here to listen. Can you tell me more about what's been going on? You can use 'I am feeling down/feeling sad because of school/friends'"
        ]
    },
    {
        "patterns": [r".*(feeling down because of my school|feeling sad because of my school|feel down because of my school|feel sad because of my school|feeling down because of school|feel down because of school|feel sad because of school|feeling sad because of school).*"],
        "responses": [        
            '''I'm sorry to hear that you're feeling down about your school. School can sometimes be challenging and overwhelming, but remember that you're not alone in feeling this way. Many students experience similar emotions at some point during their academic journey. Here are a few suggestions to help you cope with your feelings:

1. Identify the source: Try to pinpoint what specifically is making you feel down about school. Is it a particular subject, workload, social interactions, or something else? Understanding the root cause can help you address the issue more effectively.

2. Seek support: Reach out to someone you trust, such as a friend, family member, or teacher, and share your feelings with them. They may be able to provide guidance, advice, or simply lend a listening ear. Additionally, consider talking to a school counselor or therapist who can offer professional support.

3. Break tasks into smaller steps: If you're feeling overwhelmed by the workload, break your tasks into smaller, more manageable steps. This can make them feel less daunting and help you approach them one at a time, reducing stress.

4. Take breaks and practice self-care: It's important to take regular breaks and engage in activities that help you relax and recharge. Engage in hobbies, exercise, spend time in nature, or do anything that brings you joy and helps take your mind off school for a while.

5. Set realistic goals: Set realistic expectations for yourself and focus on progress rather than perfection. Celebrate small achievements along the way, as they can boost your motivation and confidence.

6. Explore learning strategies: If you're struggling with a particular subject, explore different learning strategies that might work better for you. Experiment with different study techniques, seek additional resources like online tutorials or educational videos, or consider seeking extra help from a tutor or classmate.

7. Focus on your strengths: Remind yourself of your strengths and accomplishments outside of academics. School is just one aspect of your life, and you have many other talents and qualities that make you unique and valuable.

Remember, it's okay to ask for help and take care of your well-being. You don't have to navigate these feelings alone, and with time and support, things can improve.'''
        ]
    },
    {
        "patterns": [r".*(feeling down because of my work|feeling sad because of my work|feel down because of my work|feel sad because of my work|feeling down because of work|feel down because of work|feel sad because of work|feeling sad because of work).*"],
        "responses":[
            '''I'm sorry to hear that you're feeling down because of your work. Many people go through periods of dissatisfaction or stress in their jobs, so you're not alone. It's important to address these feelings and take steps towards improving your situation. Here are a few suggestions that might help:

1. Reflect on the reasons: Take some time to identify what specifically is making you feel down about your work. Is it the tasks you're assigned, the working environment, the lack of growth opportunities, or something else? Understanding the underlying causes can help you strategize for solutions.

2. Seek support: Talk to someone you trust about your feelings, such as a close friend, family member, or mentor. Sometimes, simply sharing your thoughts and concerns can provide relief and fresh perspectives. They may be able to offer advice or support.

3. Focus on the positives: While it's natural to dwell on the negatives, try to shift your focus to the positive aspects of your work. Make a list of things you enjoy or appreciate about your job, no matter how small they may seem. This can help shift your mindset and provide a more balanced view.

4. Set realistic goals: Define what you want to achieve in your career and set realistic goals to work towards. Having clear objectives can give you a sense of purpose and motivation. Break down your goals into smaller, actionable steps, and celebrate your accomplishments along the way.

5. Explore opportunities for growth: If you feel stagnant or unfulfilled in your current position, consider seeking opportunities for growth and development. This could involve taking on new responsibilities, pursuing additional training or education, or exploring other career paths within or outside of your organization.

6. Take care of yourself: It's crucial to prioritize self-care when dealing with work-related stress. Make sure you're getting enough rest, engaging in activities you enjoy outside of work, and maintaining a healthy work-life balance. Take breaks throughout the day to recharge and engage in stress-relieving activities like exercise or meditation.

7. Consider a change: If you've exhausted all possibilities for improvement and still find yourself consistently unhappy in your work, it might be worth exploring other options. This could involve looking for a new job or considering a career change. However, it's important to carefully evaluate your situation and weigh the potential risks and benefits before making any major decisions.

Remember that it's normal to have ups and downs in your career, and it's okay to seek support and make changes when necessary.'''
        ]
    },
    {
        "patterns": [r".*(hi|hey|hello|good morning|good afternoon|good evening|good night).*"],
        "responses": [
            '''Hi, what can i help you?'''
        ]
    },
    {
        "patterns": [r".*(who are you|who made you|who make you).*"],
        "responses": [
            "Hi, I am Social Work GPT and is made and maintained by some students in KTS and the RELPLUS team"
        ]
    },
    {
        "patterns": [r".*(pressure|stress|strain|burden).*"],
        "responses": [
            "I understand that you're feeling a lot of pressure right now. It's not uncommon to experience this, especially in today's fast-paced world. It's important to acknowledge and address these feelings in a healthy way. Can you tell me a bit more about what's been causing you to feel so pressured? You can tell me by using 'work/school/homework pressure'"
        ]
    },
    {
        "patterns": [r".*(work pressure|work stress|work strain|work burden|pressure of work).*"],
        "responses": [
            '''I'm sorry to hear that work has been causing you a lot of pressure. It's not uncommon to feel overwhelmed when faced with challenging work situations or high expectations. It can be helpful to take a step back and evaluate the factors contributing to your stress. Are you feeling overwhelmed by the workload, deadlines, or the level of responsibility? It might be beneficial to prioritize tasks, break them down into smaller, manageable steps, and seek support from colleagues or supervisors if needed. Remember to take breaks, practice self-care, and set realistic expectations for yourself. If the pressure continues to persist, it might be helpful to explore strategies for managing stress or consider talking to someone who can provide guidance, such as a therapist or a mentor.'''
        ]
    },
    {
        "patterns": [r".*(homework pressure|homework stress|homework strain|homework burden|pressure of homework).*"],
        "responses": [
            '''I understand that the pressure of homework can be quite overwhelming at times. It's not uncommon to feel stressed or anxious when facing a mountain of assignments and deadlines. However, it's important to approach this pressure in a proactive and balanced manner.

Firstly, try breaking down your homework into smaller, more manageable tasks. Prioritize them based on their deadlines and importance. By creating a schedule and setting realistic goals for each task, you can better allocate your time and reduce the feeling of being overwhelmed.

It may also be helpful to create a study routine or establish a designated study space. Having a structured environment can improve focus and productivity while studying. Eliminate distractions as much as possible, such as turning off notifications on your phone or finding a quiet space where you won't be easily interrupted.

Remember to take breaks during your study sessions. Studies have shown that taking short breaks can actually enhance productivity and retention. Use these breaks to relax, stretch, or engage in activities that help clear your mind. However, be mindful not to let these breaks turn into prolonged distractions.

If you find yourself struggling with certain subjects or concepts, don't hesitate to seek help. Reach out to your teachers, classmates, or online resources for clarification or additional support. Sometimes, a fresh perspective or guidance can make a significant difference in understanding and completing your homework effectively.

Lastly, take care of your overall well-being. Make sure to get enough sleep, eat nutritious meals, and engage in physical activity. These self-care practices can help you maintain focus, reduce stress, and improve your overall academic performance.

Remember, it's important to find a balance between schoolwork and personal well-being. Don't hesitate to ask for assistance when needed and be kind to yourself throughout the process. You're capable of managing your homework pressure, and with a proactive approach and self-care, you can overcome it.'''
            ]
    },
    {
        "patterns": [r".*(dictation pressure|dictation stress|dictation strain|dictation burden|pressure of dictation).*"],
        "responses": [
            '''I understand that you're feeling pressured by dictation. Dictation can be a demanding task that requires focus and accuracy. Here are a few suggestions to help you manage the pressure:

1. Practice active listening: When someone is dictating, make sure you're actively listening to their words. Pay attention to the details and try to understand the context to ensure accurate transcription.

2. Improve your typing skills: The more proficient you are in typing, the easier it will be to keep up with the dictation. Consider taking typing courses or using online resources to enhance your typing speed and accuracy.

3. Break it down: If the dictation feels overwhelming, try breaking it down into smaller sections. Focus on transcribing one portion at a time rather than thinking about the entire task. This can help alleviate the pressure and make it more manageable.

4. Take breaks: Dictation can be mentally taxing, so it's essential to take regular breaks. Stepping away from the task for a few minutes can help you relax, clear your mind, and maintain focus when you return.

5. Ask for clarification: If you're unsure about certain words or phrases in the dictation, don't hesitate to ask for clarification. It's better to ask for clarification than to make mistakes in the transcription.

6. Prioritize self-care: Remember to take care of yourself amidst the pressure. Engage in activities that help you relax and reduce stress. Practice self-care techniques such as deep breathing, meditation, or physical exercise to help you stay calm and focused.

7. Seek support if needed: If the pressure becomes overwhelming or you're struggling to cope, consider reaching out to colleagues or supervisors for support. They may be able to offer guidance or provide resources to help you manage the dictation workload more effectively.

Remember, dictation can be challenging, but with practice and patience, you can improve your skills and reduce the pressure you feel. Take it one step at a time, prioritize self-care, and don't hesitate to seek support when needed.'''
            ]
    },
    {
        "patterns": [r".*(following me|followed by).*"],
        "responses": [
            '''*If you are talking about social media, say "## followed me in facebook/instargram/twitter/X"
            
            I understand that feeling concerned about someone following you can be distressing. It's important to prioritize your safety and take appropriate steps to address the situation. Here are a few suggestions:

1. Find a safe place: If you believe you're being followed, try to go to a public area with people around. This can discourage the person from approaching you.

2. Stay aware of your surroundings: Pay close attention to your surroundings and the people around you. If you notice the individual consistently following you, make a mental note of their appearance and any other relevant details.

3. Trust your instincts: Your intuition is a powerful tool. If you genuinely feel unsafe or threatened, it's crucial to trust your gut feelings. Don't hesitate to seek help or contact the authorities if necessary.

4. Vary your routine: Changing up your daily routine can make it harder for someone to track your movements. Consider altering your routes or transportation methods to make it more challenging for the person to follow you.

5. Inform someone you trust: Let a friend, family member, or colleague know about the situation. Sharing this information can provide a support system and help you feel safer.

6. Document incidents: If you encounter any suspicious or concerning incidents, document them, including dates, times, locations, and descriptions. This information may be useful if you decide to involve the authorities.

7. Contact the authorities: If you believe your safety is in immediate danger, don't hesitate to call emergency services. They can provide guidance and support in handling the situation.

Remember, it's essential to prioritize your safety. If you continue to feel threatened or if the situation escalates, don't hesitate to reach out for professional help or support.'''
            ]
    },
    {
        "patterns": [r".*(bullied|bullying|bully).*"],
        "responses": [
            '''I'm really sorry to hear that you're being bullied. It's an unfortunate and distressing experience, but you don't have to face it alone. Here are some steps you can take to deal with bullying:

1. Stay safe: Your safety is the top priority. If you ever feel physically threatened or in immediate danger, remove yourself from the situation and seek help from a trusted adult or authority figure.

2. Talk to someone: Reach out to someone you trust, such as a family member, friend, teacher, or school counselor. Share your experiences with them and let them know how the bullying is affecting you. They can provide support, advice, and help you navigate through the situation.

3. Keep a record: Document incidents of bullying, including dates, times, locations, and descriptions of what happened. This record can be helpful if you need to report the bullying to authorities or school officials.

4. Report the bullying: Notify a teacher, principal, or other appropriate authority figure about what's happening. Provide them with the details of the incidents and express your concerns. Schools often have policies in place to address bullying and can take appropriate action.

5. Build a support network: Surround yourself with a supportive network of friends and individuals who care about your well-being. Spending time with positive influences can help boost your self-esteem and provide emotional support.

6. Practice self-care: Engage in activities that make you feel good and help reduce stress. Take care of your physical and mental well-being by exercising, pursuing hobbies, and practicing relaxation techniques like deep breathing or meditation.

7. Develop coping strategies: Learn and practice coping strategies to deal with the emotional impact of bullying. This might include techniques like positive self-talk, visualization, or seeking professional counseling if needed.

8. Stay cyber-safe: If the bullying is happening online, take steps to protect yourself. Block or ignore the individuals involved, adjust your privacy settings, and consider reporting the behavior to the platform or website administrators.

9. Educate yourself: Learn more about bullying and its effects. Understanding why bullying happens and its impact on individuals can help you cope and develop resilience.

Remember, you deserve to be treated with respect and kindness. It may take time to address the bullying fully, but by taking these steps and reaching out for support, you're actively working toward resolving the situation.
You can also watch this video here: https://www.youtube.com/watch?v=ynTuA_tlZDE'''
            ]
    },
    {
        "patterns": [r".*(call me nickname|calling me nickname|nickname call me|to me call nickname).*"],
        "responses": [
            '''I understand that someone calling you nicknames can be bothersome or uncomfortable. It's important to address this issue assertively and communicate your feelings to the person involved. Here are a few steps you can follow:

1. Reflect on your feelings: Take a moment to understand how being called nicknames makes you feel. Are you offended, hurt, or annoyed? Knowing your emotions will help you express yourself better.

2. Communicate your boundaries: Approach the person respectfully and express that their use of nicknames is bothering you. Clearly state that you prefer to be called by your given name or any other name that you are comfortable with.

3. Explain your reasons: Share your reasons for not liking the nicknames. It could be that they are derogatory, disrespectful, or simply not representative of your identity. Help the person understand why it's important to you.

4. Request their cooperation: Ask the person to respect your boundaries and refrain from using nicknames when addressing you. Politely but firmly emphasize that their cooperation is essential for maintaining a healthy and respectful relationship.

5. Seek support if needed: If the person continues to call you nicknames despite your request, consider seeking support from a trusted friend, family member, or even a supervisor or authority figure if it's happening in a professional setting. They can provide guidance or intervene if necessary.

Remember, assertively addressing the issue can help promote understanding and respect in your relationships.'''
        ]
    },
    {
        "patterns": [r".*(what can you help me|/help|what promts can i use).*"],
        "responses": [
            "Hello there! I'm here to help you with any social and emotional concerns you may have. Whether you're feeling stressed, need someone to talk to, or have questions about relationships or personal growth, feel free to share, and I'll do my best to assist you. Remember, I'm an AI, so while I can offer support and guidance, it's always important to reach out to professionals or loved ones for more in-depth assistance when needed. How can I be of help to you today?",
            '''Here are some prompts you can use to get started:

1. How can I manage my stress and anxiety effectively?
2. I'm feeling overwhelmed and don't know where to start. How can I prioritize and organize my tasks?
3. I'm having difficulty communicating with someone important to me. How can I improve my communication skills?

Feel free to choose a prompt that resonates with you, or if there's something specific on your mind, please let me know, and we can discuss it further.'''
        ]
    },
    {
        "patterns": [r".*(How can I manage my stress and anxiety effectively?|How can I manage my stress|how can I manage my anxiety).*"],
        "responses": [
            '''Managing stress and anxiety effectively is crucial for maintaining your well-being. Here are some strategies you can try:

1. Deep Breathing and Relaxation Techniques: Practice deep breathing exercises, progressive muscle relaxation, or mindfulness meditation. These techniques can help calm your mind and body during stressful moments.

2. Regular Physical Exercise: Engaging in regular physical activity, such as walking, jogging, or yoga, can help reduce stress and anxiety. Exercise releases endorphins, which are natural mood boosters.

3. Prioritize Self-Care: Take time for self-care activities that you enjoy, such as reading, taking a warm bath, listening to music, or practicing a hobby. Prioritizing self-care helps you recharge and manage stress more effectively.

4. Time Management: Break down tasks into smaller, manageable steps and create a schedule or to-do list. Prioritize tasks based on importance and set realistic deadlines. This can help reduce overwhelm and create a sense of control.

5. Healthy Lifestyle: Maintain a balanced diet, get enough sleep, and limit caffeine and alcohol intake. Nourishing your body with healthy foods and adequate rest can positively impact your stress levels.

6. Social Support: Connect with supportive friends, family, or join support groups. Talking to someone you trust about your stress and anxiety can provide comfort and guidance.

7. Positive Thinking: Challenge negative thoughts and practice positive affirmations. Focus on your strengths and achievements, and try to reframe negative situations in a more positive light.

8. Time for Relaxation: Engage in activities that promote relaxation, such as reading, listening to calming music, or practicing deep breathing exercises. Giving yourself moments of calm can help reduce stress and anxiety.

Remember, these are general suggestions, and it's essential to find what works best for you. If your stress and anxiety persist or worsen, consider seeking support from a mental health professional who can provide more personalized guidance.'''
            ]
    },
    {
        "patterns": [r".*(I'm feeling overwhelmed and don't know where to start. How can I prioritize and organize my tasks?|how can i prioritize and organize my tasks|manage tasks).*"],
        "responses": [
            ''' I'm here to help you prioritize and organize your tasks. Here are a few steps you can take to get started:

1. Write everything down: Begin by creating a list of all the tasks you need to complete. This will help you visualize your responsibilities and ensure that nothing is forgotten.

2. Determine urgency and importance: Assess each task's urgency and importance. Urgency refers to how soon something needs to be done, while importance relates to the impact it has on your goals or well-being. Prioritize tasks that are both urgent and important, as well as those that are important but not necessarily urgent.

3. Break tasks into smaller steps: If a task seems overwhelming, try breaking it down into smaller, manageable steps. This can make it easier to tackle and provide a sense of progress as you complete each step.

4. Consider deadlines: Take note of any deadlines associated with your tasks. Prioritize those with imminent deadlines to ensure you meet them in a timely manner.

5. Consider your energy levels: Reflect on your energy levels throughout the day. If you have more energy in the morning, prioritize tasks that require focus and concentration during that time. Save simpler or less demanding tasks for when your energy naturally dips.

6. Use productivity tools: Consider utilizing productivity tools and techniques to help you stay organized. Tools like calendars, to-do lists, or project management apps can assist in keeping track of your tasks and progress.

7. Seek support if needed: If you find yourself overwhelmed despite these strategies, don't hesitate to reach out to friends, family, or colleagues for support. Sometimes sharing the load or seeking guidance can make a significant difference.

Remember, organizing and prioritizing tasks is a personal process, so feel free to adjust these steps to fit your specific needs and preferences. Take one step at a time, and don't forget to celebrate your progress along the way.'''
            ]
    },
    {
        "patterns": [r".*(I'm having difficulty communicating with someone important to me. How can I improve my communication skills?|problems of communicating).*"],
        "responses": [
            '''I understand that having difficulty in communicating with someone important to you can be challenging. Improving your communication skills is essential in maintaining healthy relationships. Here are a few suggestions to help you enhance your communication skills:

1. Active Listening: Practice active listening by giving your full attention to the person speaking. Avoid interrupting or thinking about your response while they are talking. Show genuine interest by maintaining eye contact, nodding, and providing verbal cues that you are attentive.

2. Empathy and Understanding: Try to put yourself in the other person's shoes and understand their perspective. Empathy allows you to connect with their emotions and experiences, fostering a deeper level of understanding and trust.

3. Clarify and Ask Questions: If you are unsure about something the other person said, don't hesitate to ask for clarification. This shows that you are genuinely interested in understanding their point of view and helps avoid misunderstandings.

4. Non-Verbal Communication: Pay attention to your body language and non-verbal cues. Maintain an open posture, use appropriate facial expressions, and be mindful of your tone of voice. Non-verbal cues can greatly impact how your message is perceived.

5. Practice Reflective Communication: Reflective communication involves summarizing and paraphrasing what the other person said to ensure that you've understood them correctly. This not only confirms your understanding but also demonstrates active engagement in the conversation.

6. Be Mindful of Timing: Choose an appropriate time and place for important conversations. Make sure both you and the other person are in a calm and receptive state of mind. Avoid discussing sensitive topics when either of you is stressed or distracted.

7. Practice Patience and Understanding: Remember that effective communication takes time and effort. Be patient with yourself and the other person. It's okay to make mistakes and learn from them.

8. Seek Professional Help: If you are experiencing significant difficulties in your communication, consider seeking guidance from a professional, such as a therapist or counselor. They can provide you with personalized strategies and support.

Remember, improving communication skills is an ongoing process. With practice and patience, you can develop stronger connections and create healthier relationships.'''
        ]
    },
    {
        "patterns": [r".*\b(?:I'm feeling down|I'm feeling sad|I'm depressed)\b.*"],
        "responses": [
            "I'm here to listen. Can you tell me more about what's been going on?",
            "I'm sorry to hear that. Would you like to talk about what's been bothering you?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm feeling anxious|I'm feeling stressed|I'm overwhelmed)\b.*"],
        "responses": [
            "It's understandable to feel that way. Is there something specific causing your anxiety or stress?",
            "Take a deep breath. Is there anything you'd like to share about what's been overwhelming you?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm having trouble sleeping|I can't sleep|Insomnia)\b.*"],
        "responses": [
            "I'm sorry to hear that. Sleep difficulties can be challenging. Have you tried any relaxation techniques before bed?",
            "Establishing a bedtime routine can help improve sleep. Would you like some suggestions?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm having relationship problems|relationship advice|relationship trouble)\b.*"],
        "responses": [
            "Relationships can be complex. Can you provide more details about the issues you're facing?",
            "I'm here to help. Understanding the dynamics of the relationship can be a good starting point. Can you tell me more?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm feeling lonely|I need social connection|I'm isolated)\b.*"],
        "responses": [
            "Loneliness can be difficult to cope with. Have you considered reaching out to friends or engaging in social activities?",
            "Connecting with others can help alleviate feelings of loneliness. Is there something specific you're looking for in terms of social connection?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm feeling overwhelmed at work|work stress|work-life balance)\b.*"],
        "responses": [
            "Work-related stress can take a toll. It's important to find a healthy balance. What aspects of work are causing you to feel overwhelmed?",
            "Achieving a work-life balance is crucial. Can you share more details about the challenges you're facing?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm experiencing grief|bereavement|loss)\b.*"],
        "responses": [
            "I'm sorry for your loss. Grief can be a difficult journey. Would you like to talk about your feelings or share any memories?",
            "Losing someone can be incredibly hard. Is there anything specific you're struggling with in the grieving process?"
        ]
    },
    {
        "patterns": [r".*\b(?:I need help with self-care|self-care tips|taking care of myself)\b.*"],
        "responses": [
            "Self-care is important for your well-being. What are some activitiesor practices you enjoy or would like to explore?",
            "Making time for self-care is vital. Is there a particular area of self-care you'd like guidance on?"
        ]
    },
    {
        "patterns": [r".*\b(?:I need advice on setting boundaries|boundary setting|assertiveness)\b.*"],
        "responses": [
            "Setting boundaries is crucial for healthy relationships. What specific situations or relationships are you having trouble with?",
            "Establishing boundaries can be challenging. Can you provide more context about the issues you're encountering?"
        ]
    },
    {
        "patterns": [r".*\b(?:I'm interested in therapy|therapist recommendations|finding a therapist)\b.*"],
        "responses": [
            "Therapy can be beneficial. Are you looking for a specific type of therapy or recommendations in your area?",
            "Finding the right therapist is important. Is there a particular issue you'd like to address through therapy?"
        ]
    }
            
        ]

    def clear_placeholder(self, event):
        self.user_input_entry.clear()

    def handle_user_input(self):
        user_input = self.user_input_entry.text().lower()
        self.user_input_entry.clear()

        matched_rules = []
        for rule in self.rules:
            matched_patterns = [pattern for pattern in rule["patterns"] if re.search(pattern, user_input)]
            if matched_patterns:
                matched_rules.append(rule)

        if matched_rules:
            rule = random.choice(matched_rules)
            response = random.choice(rule.get("responses", [""]))
        else:
            response = "I'm sorry, I didn't understand that. For more general questions, Chat Whatever might help you!"

        self.conversation_text.append("User: " + user_input)
        self.conversation_text.append("Social Work GPT: " + response)
        self.conversation_text.append("")

        if user_input in ["bye", "exit"]:
            QtCore.QCoreApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec_())