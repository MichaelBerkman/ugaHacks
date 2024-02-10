with open(coral_file_path,
                                      "r") as file:  # this sees if the link has already been clicked
                                contents = file.read()

                                if href_value not in contents:
                                    with open(coral_file_path,
                                              "a") as file:  # if link hasnt been clicked this adds it to the list and closes the file
                                        # Write the link to the file
                                        file.write(href_value + '\n')
                                        file.close()
                                        element_found = True



current_directory = os.getcwd()
pgalnamer_file = "pgalnamer.txt"
pgalnamer_path = "/home/michaelberkman/Desktop/ChaelCam/"
photoname = 0

with open(pgalnamer_path,
                                      "r") as file:  # this sees if name is already used 
                                contents = file.read()

                                if photoname not in contents:
                                    with open(pgalnamer_path,
                                              "a") as file:  #if name not in list
                                        # Write the link to the file
                                        file.write(photoname + ".jpg" + '\n')
                                        file.close()
                                
                                if photoname in contents:
                                        with open(pgalnamer_path,
                                            "a") as file:
                                        photoname+1
                                        file.write(photoname + ".jpg" + '\n')
                                        file.close()
                                        
                                        
