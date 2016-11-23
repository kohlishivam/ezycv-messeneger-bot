from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Image
from django.http import HttpResponse
import urllib2
from django.utils.decorators import method_decorator
import json
import requests
from chatbot.models import event,resume_input


# Create your views here.

sender_id = 'ba'
VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAATyjn0ZCjToBAPlBoFFXhLdZBUy9nXZAsOeZBNWu7x0BZBFrxFZAWXyCL3rmWZAETrRzAj4HAhZAxtrzK05Oef0Ul3kZBOZCHuN5ZCHrbI8yRAyIt8ZCEqwbe6TaxMgpELesq34BHmNGDy5Rhmv8OwUwNHZAqXAKdLIY5CS2Iqv4trggMAZDZD'


def userdeatils(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data         

        

def post_facebook_message(fbid,message_text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    
    if message_text == 'templates':
        response_msg = cards(fbid)

    elif message_text == 'selection' :
        response_msg = selectcard(fbid)

    elif message_text == 'resume download':
        response_msg = card_resume(fbid) 

    elif message_text == 'options':
        response_msg = quickreply(fbid)

    elif message_text == 'options_skills':
        response_msg = quickreply_skills(fbid)

    elif message_text == 'options_qualification':
        response_msg = quickreply_qualification(fbid)

    elif message_text == 'options_experience':
        response_msg = quickreply_experience(fbid)

    elif message_text == 'options_HOBBIES':
        response_msg = quickreply_HOBBIES(fbid)



    

    else:
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})

    requests.post(post_message_url, 
                    headers={"Content-Type": "application/json"},
                    data=response_msg)




def card_resume(fbid):
    
    response_object = {
      "recipient": {
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "template",
          "payload": {
            "template_type": "generic",
            "elements": [{
              "title": "RESUME",
              "subtitle": "Don,t wait just click",
              "item_url": "https://ezycvtester.herokuapp.comresume/%s"%(fbid),               
              "item_url": "https://ezycvtester.herokuapp.com/resume/%s"%(fbid),               
              "image_url": "https://placeholdit.imgix.net/~text?txtsize=50&txt=Download%20Resume&w=400&h=500",
              "buttons": [{
                "type": "web_url",
                "url": "https://ezycvtester.herokuapp.com/resume/%s"%(fbid),  
                "title": "DOWNLOAD"
              }, {
                "type": "element_share"
              }]
              
            }]
          }
        }
      }
    }

    return json.dumps(response_object)




def cards(fbid):
    
    response_object = {
      "recipient": {
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "template",
          "payload": {
            "template_type": "generic",
            "elements": [{
              "title": "party theme",
              "subtitle": "party,fests,weddings,birthdays etc",
              "item_url": "https://myresumemaker.herokuapp.com/temp1/%s"%(fbid),               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/l/t35.0-12/14800069_1785774908361060_98733447_o.png?oh=5e3268cb388a25f6d84cb2c27b3c757f&oe=580A723E",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp1/%s"%(fbid),
                "title": "Open your website in this theme"
              }, {
                "type": "element_share"
              }],
            }, {
              "title": "hackathon theme",
              "subtitle": "all tech competitions them",
              "item_url": "https://myresumemaker.herokuapp.com/temp2/%s"%(fbid),               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/t35.0-12/14795941_1785774938361057_1017427262_o.png?oh=6809b9c14ee2646703a8047da8b2c479&oe=580A89BA",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp2/%s"%(fbid),
                "title": "Open your website in this theme"
              }, {
                "type": "element_share"
                
              }]
            }]
          }
        }
      }
    }

    return json.dumps(response_object)

def selectcard(fbid):
    response_object ={
  "recipient":{
    "id":fbid
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title":"Resume",
            
            "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=Resume&w=450&h=500",
            "subtitle":"Make a resume",
            "buttons":[
              
              {
                "type":"postback",
                "title":"Resume",
                "payload":"RESUME"
              }              
            ]
          },
          {
            "title":"Event Website",
            
            "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=Event%20Website&w=450&h=500",
            "subtitle":"Make an Event website",
            "buttons":[
              
              {
                "type":"postback",
                "title":"event-website",
                "payload":"EVENT"
              }              
            ]
          }


        ]
      }
        }
      }
    }
    return json.dumps(response_object)



class MyChatBotView(generic.View):
    def get (self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Oops invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        global sender_id
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        print  incoming_message
        

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                print message
                try:
                    
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    a= userdeatils(sender_id)
                    p = event.objects.get_or_create(fbid =sender_id)[0]
                    pp = resume_input.objects.get_or_create(fbid =sender_id)[0]
                    name = '%s %s'%(a['first_name'],a['last_name'])
                    if message_text.lower() in 'hi,hello,hey,supp'.split(','):

                        print  'hihihihihihihihihih'+ sender_id
                        post_facebook_message(sender_id,'Hey , ' + name +', This is a automated chatting software it will ask u your details about your resume or event website and in the end voila u will get ypur own e-resume pdf resume or a website of your event. Lets get started by selecting what u want to make today ')
                        post_facebook_message(sender_id,'selection')

                    elif message_text == 'options':
                        post_facebook_message(sender_id,'options')

                           
                            
                    elif p.state =='1':

                        p.name = message_text
                        p.state='2'
                        p.save()
                        print  'hihihihihihihihihih'+ sender_id
                        post_facebook_message(sender_id,'great ,Now  Please tell me your contact phone number to be displayed on the page ')
         
                    elif p.state =='2':

                        p.contact = message_text
                        p.state='3'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your tagline  for the event  ')

                    elif p.state =='3':
                        p.tagline = message_text
                        p.state='4'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your start date  for the event  in dd/mm/yy format ')

                    elif p.state =='4':
                        p.datestart = message_text
                        p.state='5'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your end date  for the event dd/mm/yy format ') 

                    elif p.state =='5':
                        p.dateend = message_text
                        p.state='6'
                        p.save()
                        post_facebook_message(sender_id,' Now, Please tell me your organiser name to be displayed on the page ')   

                    elif p.state =='6':
                        p.oname = message_text
                        p.state='7'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell me your conatct email id  to be displayed on the page ')                                              

                    elif p.state =='7':
                        p.emailid = message_text
                        p.state='8'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell if u have any twitter id  if yes send its link otherwise just send no  ')

                    elif p.state =='8':
                        p.twitterlink = message_text
                        p.state='9'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell if u have any fabeook page if yes send its link otherwise just send no  ')                                             
                    

                    elif p.state =='9':
                        p.fblink = message_text
                        p.state='10'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me description of the event ')                     

                    elif p.state =='10':
                        p.description = message_text
                        p.state='11'
                        p.save()
                        post_facebook_message(sender_id,'if u have a logo please send its link if not just send no ')                             

                    elif p.state =='11':
                        p.logolink = message_text
                        p.state='12'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me location of the event in one line seperated by commas  ')    

                    elif p.state =='12':
                        p.location = message_text
                        p.state='13'
                        p.save()
                        post_facebook_message(sender_id,'send me the details of the 1st sub event  ') 

                    elif p.state =='13':
                        p.sub1 = message_text
                        p.state='14'
                        p.save()
                        post_facebook_message(sender_id,' Send me the details of the 2st sub event  ') 
                    
                    elif p.state =='14':
                        p.sub2 = message_text
                        p.state='15'
                        p.save()
                        post_facebook_message(sender_id,' Send me the details of the 3st sub event  ')

                    elif p.state =='15':
                        p.sub3 = message_text
                        p.state='16'
                        p.save()
                        post_facebook_message(sender_id,' Send me the details of the 4st sub event  ')
                        print 'hi hi hi hi hi hi ' + sender_id
                        print 'hi hi hi hi hi hi ' + sender_id
                        print 'hi hi hi hi hi hi ' + sender_id
                        print 'hi hi hi hi hi hi ' + sender_id
                        print 'hi hi hi hi hi hi ' + sender_id
                        

                    elif p.state =='16':
                        p.sub4 = message_text
                        p.state='17'
                        p.save()
                        print sender_id
                        

                        post_facebook_message(sender_id,' Please select one of the templates given below ')
                        post_facebook_message(sender_id,'Templates')                        
                        


                        
                    elif pp.state =='1':
                        pp.emailid = message_text
                        pp.state='3'
                        pp.save()
                        post_facebook_message(sender_id,'Your date of birth')
                       
                        
                    elif pp.state =='3':
                        pp.dob = message_text
                        pp.state='4'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now  Please tell me your contact PHONE NUMBER to be displayed on the resume ')
                    
                    elif pp.state =='4':
                        pp.contact = message_text
                        pp.state='5'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now  Please provide me your LinkedIn id')

                    elif pp.state =='5':
                        pp.LinkedIn = message_text
                        pp.state='6'
                        pp.save()
                        post_facebook_message(sender_id,'Now your city of residence')
         

                    elif pp.state =='6':
                        pp.city = message_text
                        pp.state='7'
                        pp.save()
                        post_facebook_message(sender_id,'okay, now your Summary or Objective. ')

 
                    elif pp.state == '7':
                        pp.objective_line1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')

                    elif pp.state == '1111':
                        pp.skills_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1112':
                        pp.skills_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1113':
                        pp.skills_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1114':
                        pp.skills_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1121':
                        pp.educational_qualifications_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1122':
                        pp.educational_qualifications_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1123':
                        pp.educational_qualifications_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1124':
                        pp.educational_qualifications_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1131':
                        pp.experience_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1132':
                        pp.experience_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1133':
                        pp.experience_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1134':
                        pp.experience_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1141':
                        pp.hobbies_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1142':
                        pp.hobbies_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1143':
                        pp.hobbies_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1144':
                        pp.hobbies_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')

                    
                    
                    

                except Exception as e:
                    print e
                    pass

                    
                try:
                    if 'postback' in message:
                        handle_postback(message['sender']['id'],message['postback']['payload'])
                        return HttpResponse()
                    else:
                        pass

                except Exception as e:
                    print e
                    pass 



                  
                try:
                    if 'quick_reply' in message['message']:
                        handle_quickreply(message['sender']['id'],
                        message['message']['quick_reply']['payload'])
                        return HttpResponse()
                    else:
                        pass
                except Exception as e:
                    print e
                    pass  


            return HttpResponse()

def quickreply_HOBBIES(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"HOBBIES_1",
                                "payload":"add_HOBBIES_1"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_2",
                                "payload":"add_HOBBIES_2"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_3",
                                "payload":"add_HOBBIES_3"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_4",
                                "payload":"add_HOBBIES_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_HOBBIES"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)
def quickreply_experience(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"experience_1",
                                "payload":"add_experience_1"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_2",
                                "payload":"add_experience_2"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_3",
                                "payload":"add_experience_3"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_4",
                                "payload":"add_experience_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_experience"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def quickreply_skills(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"skills_1",
                                "payload":"add_skills_1"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_2",
                                "payload":"add_skills_2"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_3",
                                "payload":"add_skills_3"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_4",
                                "payload":"add_skills_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_skills"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def quickreply_qualification(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"qualification_1",
                                "payload":"add_qualification_1"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_2",
                                "payload":"add_qualification_2"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_3",
                                "payload":"add_qualification_3"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_4",
                                "payload":"add_qualification_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_qualification"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def handle_quickreply(fbid,payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    output_text = 'Payload Recieved: ' + payload

    if payload == 'skills':
        return post_facebook_message(fbid,'options_skills')

    elif payload == 'done_skills':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_skills_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1111'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1112'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1113'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1114'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')


    
    elif payload == 'educational qualifications':
        return post_facebook_message(fbid,'options_qualification')

    elif payload == 'done_qualification':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_qualification_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1121'
        pp.save()
        return post_facebook_message(fbid,'Enter your qualification')

    elif payload == 'add_qualification_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1122'
        pp.save()
        return post_facebook_message(fbid,'Enter your qualification')

    elif payload == 'add_qualification_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1123'
        pp.save()
        return post_facebook_message(fbid,'Enter your qualification')

    elif payload == 'add_qualification_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1124'
        pp.save()
        return post_facebook_message(fbid,'Enter your qualification')



    if payload == 'experience':
        return post_facebook_message(fbid,'options_experience')

    elif payload == 'done_experience':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_experience_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1131'
        pp.save()
        return post_facebook_message(fbid,'Enter your experience,detailing about your tittle')

    elif payload == 'add_experience_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1132'
        pp.save()
        return post_facebook_message(fbid,'Enter your experience')

    elif payload == 'add_experience_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1133'
        pp.save()
        return post_facebook_message(fbid,'Enter your experience')

    elif payload == 'add_experience_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1134'
        pp.save()
        return post_facebook_message(fbid,'Enter your experience')


    if payload == 'HOBBIES':
        return post_facebook_message(fbid,'options_HOBBIES')

    elif payload == 'done_HOBBIES':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_HOBBIES_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1141'
        pp.save()
        return post_facebook_message(fbid,'Enter your HOBBIES,detailing about your tittle')

    elif payload == 'add_HOBBIES_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1142'
        pp.save()
        return post_facebook_message(fbid,'Enter your HOBBIES')

    elif payload == 'add_HOBBIES_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1143'
        pp.save()
        return post_facebook_message(fbid,'Enter your HOBBIES')

    elif payload == 'add_HOBBIES_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1144'
        pp.save()
        return post_facebook_message(fbid,'Enter your HOBBIES')


    if payload == 'finish':
        return post_facebook_message(fbid,'resume download')



def quickreply(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"SKILLS",
                                "payload":"skills"
                              },
                              {
                                "content_type":"text",
                                "title":"QUALIFICATIONS",
                                "payload":"educational qualifications"
                              },
                              {
                                "content_type":"text",
                                "title":"EXPERIENCE",
                                "payload":"experience"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES",
                                "payload":"HOBBIES"
                              },
                              {
                                "content_type":"text",
                                "title":"IM DONE",
                                "payload":"finish"
                              }
                            ]
                          }
                        }
    return json.dumps(response_object)

def resume(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mycv.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    pp = resume_input.objects.get_or_create(fbid=id)[0]
    #print dir(p)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    a= userdeatils(sender_id)
    pp.name = '%s %s'%(a['first_name'],a['last_name'])




    p.setFont("Helvetica", 20)
    p.drawString(230,820, pp.name)
    p.setFont("Helvetica", 8)
    p.drawString(230,810,pp.emailid)
    p.drawString(230,800,pp.contact)
    p.drawString(230,790,pp.dob)
    p.drawString(230,780,pp.LinkedIn)
    p.drawString(230,770,pp.city)
    p.setFont("Helvetica", 13)
    
    p.drawString(0,750,"Objective")
    p.setStrokeColor(colors.red)    
    p.line(0,745,500,745)
    p.setFont("Helvetica", 9)
    p.drawString(20,735,pp.objective_line1)
    p.drawString(20,725,pp.objective_achievements)

    p.setFont("Helvetica", 13)
    p.drawString(0,705,"Educational Qualifications ")
    p.setStrokeColor(colors.red)    
    p.line(0,700,500,700)
    p.setFont("Helvetica", 9)
    p.drawString(20,690,pp.educational_qualifications_1)
    p.drawString(20,680,pp.educational_qualifications_2)
    p.drawString(20,670,pp.educational_qualifications_3)
    p.drawString(20,660,pp.educational_qualifications_4)
    
    p.drawString(0,640,"Experience")
    p.setStrokeColor(colors.red)    
    p.line(0,635,500,635)
    p.setFont("Helvetica", 9)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,605,pp.experience_1)
    p.drawString(20,595,pp.experience_1)

    p.setFont("Helvetica", 13)
    p.drawString(0,575,"Skills")
    p.setStrokeColor(colors.red)    
    p.line(0,570,500,570)
    p.setFont("Helvetica", 9)
    p.drawString(20,560,pp.skills_1)
    p.drawString(20,550,pp.skills_2)
    p.drawString(20,540,pp.skills_3)
    p.drawString(20,530,pp.skills_4)
    
    p.setFont("Helvetica", 13)
    p.drawString(0,510,"Hobbies")
    p.setStrokeColor(colors.red)    
    p.line(0,505,500,505)
    p.setFont("Helvetica", 9)
    p.drawString(20,495,pp.hobbies_1)
    p.drawString(20,485,pp.hobbies_2)
    p.drawString(20,475,pp.hobbies_3)
    p.drawString(20,465,pp.hobbies_4)

    p.showPage()
    p.save()
    return response

def index(request):
    set_menu()
    handle_postback('fbid','MENU_WHY')
    context_dict = {}
    context_dict['fbid'] = sender_id
    return render(request,'chatbot/index.html', context_dict)

def eventweb(request,id):
    #fbid = '1047867078643788'


    p = event.objects.get_or_create(fbid =id)[0]
    name = p.name 
    location = p.location
    logolink = p.logolink  
    description = p.description
    fblink = p.fblink  
    emailid = p.emailid  
    oname = p.oname 
    dateend = p.dateend 
    datestart =  p.datestart  
    contact = p.contact 
    tagline = p.tagline
    twitterlink = p.twitterlink
    sub1 = p.sub1
    sub2 = p.sub2
    sub3 = p.sub3
    sub4 = p.sub4

    context_dict = {}
    context_dict['eventname'] = name 
    context_dict['location'] = location
    context_dict['logolink'] = logolink
    context_dict['description'] = description
    context_dict['fblink'] = fblink
    context_dict['emailid'] = emailid
    context_dict['organisername'] = oname
    context_dict['dateend'] = dateend
    context_dict['datestart'] = datestart
    context_dict['contact'] = contact
    context_dict['tagline'] = tagline
    context_dict['twitterlink'] = twitterlink
    context_dict['sub1'] = sub1
    context_dict['sub2'] = sub2
    context_dict['sub3'] = sub3
    context_dict['sub4'] = sub4



    return render(request,'chatbot/temp1.html',context_dict)

def eventweb2(request,id):
    #fbid = '1047867078643788'

    p = event.objects.get_or_create(fbid = id)[0]
    name = p.name 
    location = p.location
    logolink = p.logolink  
    description = p.description
    fblink = p.fblink  
    emailid = p.emailid  
    oname = p.oname 
    dateend = p.dateend 
    datestart =  p.datestart  
    contact = p.contact 
    tagline = p.tagline
    twitterlink = p.twitterlink
    sub1 = p.sub1
    sub2 = p.sub2
    sub3 = p.sub3
    sub4 = p.sub4

    context_dict = {}
    context_dict['eventname'] = name 
    context_dict['location'] = location
    context_dict['logolink'] = logolink
    context_dict['description'] = description
    context_dict['fblink'] = fblink
    context_dict['emailid'] = emailid
    context_dict['organisername'] = oname
    context_dict['dateend'] = dateend
    context_dict['datestart'] = datestart
    context_dict['contact'] = contact
    context_dict['tagline'] = tagline
    context_dict['twitterlink'] = twitterlink
    context_dict['sub1'] = sub1
    context_dict['sub2'] = sub2
    context_dict['sub3'] = sub3
    context_dict['sub4'] = sub4



    return render(request,'chatbot/temp2.html',context_dict)

def eventreg(request):
    context_dict = {}

    return render(request,'chatbot/shop.html',context_dict)

def set_menu():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
    
    response_object =   {
                          "setting_type" : "call_to_actions",
                          "thread_state" : "existing_thread",
                          "call_to_actions":[
                            {
                              "type":"postback",
                              "title":"Your event website",
                              "payload":"MENU_OUTPUT"
                            },
                            {
                              "type":"postback",
                              "title":"Our website",
                              "payload":"MENU_LINK"
                            },
                            {
                              "type":"postback",
                              "title":"Why Master Event",
                              "payload":"MENU_WHY"
                            }
                          ]
                        }

    menu_object = json.dumps(response_object)
    status = requests.post(post_message_url,
          headers = {"Content-Type": "application/json"},
          data = menu_object)

def handle_postback(fbid,payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    output_text = 'Payload Recieved: ' + payload

    if payload == 'MENU_WHY':
        return post_facebook_message(fbid,'Your vision our creativity')

    elif payload == 'MENU_LINK':
        return post_facebook_message(fbid,'Master-Event.github.io')
        

    elif payload == 'MENU_OUTPUT':
        return post_facebook_message(fbid,'https://myresumemaker.herokuapp.com/temp2')





    elif payload == "EVENT" :
        p = event.objects.get_or_create(fbid =fbid)[0]
        p.state = '1'
        p.greetings = 'TRUE'

        p.save()

        return post_facebook_message(fbid,'please tell me your event name ')

    elif payload == "RESUME" :
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1'
        pp.greetings = 'TRUE'
        pp.save()

        return post_facebook_message(fbid,'Please tell me your email id ')  


                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg) 





















