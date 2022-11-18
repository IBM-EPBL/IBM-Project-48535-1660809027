import cv2
import opencv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-2fu81eolfhmrt4amjgvuum0xqvg9zcsmsr54gktl4c0x','1b45e808a0a4ae5a892572cc205c612c')
service=CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-2fu81eolfhmrt4amjgvuum0xqvg9zcsmsr54gktl4c0x:1b45e808a0a4ae5a892572cc205c612c@031d65ea-9d17-4c71-bca3-015e317a17c4-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame=cap.read()
    decodedObjects=pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data",obj.data)
        a=obj.data.decode('UTF-8')
        cv2.putText(frame,"Ticket",(50,50),font,2,
                    (255,0,0),3)
        #print(a)
        try:
            response=service.get_document(
                db ='booking',
                doc_id = a
              ).get_result()
            print(response)
            time.sleep(5)
        except Exception as e:
            print("Not a Valid Ticket")
            time.sleep(5)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
