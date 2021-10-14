<template>
    <div>
        <Header/>

        <!--<Homepage/>
       -->
        <section id="contact" class="contact">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>Create Course</h2>
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
                    <label for="name">Course ID:</label>
                    <input
                      type="text"
                      class="form-control"
                      name="subject"
                      id="subject"
                      required
                    />
                  </div>

                  <div class="form-group">
                    <label for="name">Course Name:</label>
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
                  <label for="name">Course Description:</label>
                  <textarea
                    class="form-control"
                    name="message"
                    rows="10"
                    required
                  ></textarea>
                </div>

                <div class="form-group">
                  <label for="name">Prerequisite:</label>
                  <textarea
                    class="form-control"
                    name="message"
                    rows="10"
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
            <a href="#" class="classCreate-btn">Create Course</a>
        </div>
        <div class="cancel">
            <a href="ViewCourse" class="cancel-btn">Cancel</a>
        </div>
      </div>








    </div>


</template>

<script>
</script>
