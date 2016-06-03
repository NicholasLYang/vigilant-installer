# vigilant-installer
Installer for vigilant web gallery


Here's how the admin tools works. It calls the api using the function callApi(). The standard format for a url is 107.170.107.124/function/key/arg1/arg2 (the ip I still need to figure out how to customize for the server). The response (if there is one) should be in JSON, which you should then parse into a friendly output. The way you choose functions is as follows. The script will print out:

0 Delete Image
1 Delete Gallery
2 List Galleries
3 Archive Year

The user should input a number and get the function. If you are deleting an image or a gallery, you should list the potential galleries/images. You can list the galleries/images by requesting them through the API. Follow up questions will get the args and then you can call the API. Always end delete functions with "Gallery x is deleted" or "Image x from gallery y has been deleted"