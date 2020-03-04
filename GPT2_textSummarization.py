"""
pip install bert-extractive-summarizer
pip install spacy==2.0.12
pip install transformers==2.2.0
"""

from summarizer import Summarizer,TransformerSummarizer

body = '''
Eight people are dead following two shootings at shisha bars in the western German city of Hanau. At least five people were injured after gunmen opened fire at about 22:00 local time (21:00 GMT), police told the BBC. Police added that they are searching for the suspects, who fled the scene and are currently at large. The first shooting was at a bar in the city centre, while the second was in Hanau's Kesselstadt neighbourhood, according to local reports. Police officers and helicopters are patrolling both areas. An unknown number of gunmen killed three people at the first shisha bar, Midnight, before driving to the Arena Bar & Cafe and shooting dead another five victims, regional broadcaster Hessenschau reports. A dark-coloured vehicle was then seen leaving the scene.The motive for the attack is unclear, a police statement said. Can-Luca Frisenna, who works at a kiosk at the scene of one of the shootings said his father and brother were in the area when the attack took place. It's like being in a film, it's like a bad joke, that someone is playing a joke on us, he told Reuters.I can't grasp yet everything that has happened. My colleagues, all my colleagues, they are like my family - they can't understand it either. Hanau, in the state of Hessen, is about 25km (15 miles) east of Frankfurt. It comes four days after another shooting in Berlin, near a Turkish comedy show at the Tempodrom concert venue, which killed one person.'''

model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
result = model(body, min_length=60)
full = ''.join(result)
print(full)

