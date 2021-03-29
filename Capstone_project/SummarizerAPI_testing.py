import requests
response = requests.get(
    "http://0.0.0.0:4444/Textsummary/abstractive",
    data={
        #'text': 'Chandrababu Naidu has freshly given a warning to all the ex Ministers and official representatives of his party not to give any Live interviews to NTV and TV9. The reason he cited was running some negative stories about Nimmagadda Ramesh Kumar in those two channels. It is almost like a Check Post by Chandrababu. He is the decision maker to allow anyone from his party to any channel. Sources say that Chandrababu must be afraid that his party men will be cornered by the interviewers and callers during the Live Interviews as those channels exposed their party stand with respect to Nimmagadda. It is pity that TDP is not just afraid of elections but also the TV interviews. It is better to wind up such a timid and spineless political party", commented a YSRCP representative knowing this news.'
         'text': "Increasing human intervention in ecologically sensitive Himalayan region is making it more vulnerable to climate change, environment experts said on Sunday as a glacier broke off at Joshimath in Uttarakhand's Chamoli district, triggering massive flood in the state. The glacier burst triggered massive flood in the Dhauli Ganga river and caused large-scale devastation in the upper reaches of Himalayas.Over 150 labourers working at a power project in Tapovan-Reni are feared dead, an Indo-Tibetan Border Police spokesperson said while quoting the project-in charge. Three bodies have been recovered so far. It is an unfortunate incident. Our thoughts are with the missing construction workers and affected people of Uttarakhand. While exact cause of this incident is yet to be ascertained and needs an honest investigation, it is evident that increasing human interventions in ecologically sensitive Himalayan region are making it more vulnerable to climate change.Heavy construction work in the fragile eco-sensitive zones should be avoided, Avinash Chanchal, senior climate and energy campaigner, Greenpeace India said. Another expert, Anjal Prakash, one of the lead authors of a special report on oceans and cryosphere of the Intergovernmental Panel on Climate Change (IPCC), said while it was too early to explain the cause of the devastation, prima facie it seemed to be due to climate change and global warming which has become an alarming and irreversible situation now.He also said that Himalayan region is the least monitored region and requires the government to spend more resources in tracking these areas closely so that there is more awareness. Himalayan region is the least monitored region and this event actually shows how vulnerable we could be. I would request the government to spend more resources in monitoring the region better so that we have more information about the change process. The result would be that we are more aware and could develop better adaptation practices, Prakash, who is also a Research Director and Adjunct Associate Professor at the Indian School of Business (ISB), Hyderabad, said.Terming the glacier burst as a rare incident, Mohd Farooq Azam, Assistant Professor, Glaciology and Hydrology, IIT Indore said satellite and Google Earth images do not show a glacial lake near the region, but there is a possibility of a water pocket. It is a rare incident for a glacial burst to happen. Satellite and Google Earth images do not show a glacial lake near the region, but there is a possibility that there may be a water pocket in the region. Water pockets are lakes inside the glaciers, which may have erupted leading to this event. We need further analysis, weather reports and data to confirm if this indeed was the case, he said.Azam further said the thermal profile of ice is increasing, as earlier the temperature of ice ranged from -6 to -20 degree Celsius, it is now -2 degrees, making it more susceptible to melting. It is unlikely that this was a cloud burst since weather reports in Chamoli district show sunny weather till today with no record of precipitation. There is no doubt that global warming has resulted in the warming of the region.Climate change-driven erratic weather patterns like increased snowfall and rainfall, and warmer winters have led to the melting point of a lot of snow, he said. Greenpeace India's Chanchal said there was a need to rethink about the current development model for the Himalayan region.In 2013, Uttarakhand saw similar incident because of glacial lake outburst flood (GLOF). Researchers said this happened because of global warming which is leading to melting glaciers. They also had warned that such events might happen more frequently in the future. To tackle this, we need to rethink about the current development model for Himalaya region. It cannot happen at the cost of environment and local communities, Chanchal said."
    },
    
)
print(response.json())