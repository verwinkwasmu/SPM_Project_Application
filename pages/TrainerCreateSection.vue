<template>
    <div>
        <TrainerHeader/>

        <!--<Homepage/>
       -->
        <section id="contact" class="contact">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>Create Section</h2>
          </div>
            
          <div class="row">
            
         
            <div class="col-lg-8" id="createCourse">
              <form
                action="forms/contact.php"
                method="post"
                role="form"
                class="php-email-form"
              >
                <div class="row">
                  
                  <div class="form-group">
                    <label for="name">Section Name: </label>
                    <input
                      type="text"
                      class="form-control"
                      name="subject"
                      id="subject"
                      required
                    />
                  </div>


                    
                </div>

                <div class="form-group">
                <!-- <b-field class="file is-primary" :class="{'has-name': !!file}">
                    <b-upload v-model="file" class="file-label">
                        <span class="file-cta">
                            <b-icon class="file-icon" icon="upload"></b-icon>
                            <span class="file-label">Click to upload: </span>
                        </span>
                        <span class="file-name" v-if="file">
                            {{ file.name }}
                        </span>
                    </b-upload>
                </b-field> -->

                  <label for="name">Uploaded: </label>
                <b-field class="file is-primary" :class="{'has-name': !!file}">
                    <b-upload v-model="file" class="file-label">
                        <span class="file-cta">
                            <!-- <b-icon class="file-icon" icon="upload"></b-icon> -->
                            <!-- <span class="file-label">Click to upload: </span> -->
                        </span>
                        <span class="file-name" v-if="file">
                            {{ file.name }}
                        </span>
                    </b-upload>
                </b-field>
                </div>

                <div class="form-group">
                  <label for="name">Lesson Video Link: </label>
                  <textarea
                    class="form-control"
                    name="message"
                    rows="1"
                    required
                  ></textarea>
                </div>
             
              </form>
              
            </div>


            
          </div>
        </div>





      </section>

      <div class="buttongroup">
        <div class="classCreate">
            <a href="#" class="classCreate-btn">Create Section</a>
        </div>
        <div class="cancel">
            <a href="ViewCourse" class="cancel-btn">Cancel</a>
        </div>
      </div>








    </div>


</template>

<script>
    export default {
            data() {
                return {
                    file: null
                }
            }
        }
</script>
