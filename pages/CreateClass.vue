<template>
    <div>
        <Header/>

        <!--<Homepage/>
       -->
        <section id="contact" class="contact">
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>Create Class</h2>
          </div>
            
          <div class="row">
            
         
            <div class="col-lg-6 mt-5 mt-lg-0 d-flex align-items-stretch">
              <form
                action="forms/contact.php"
                method="post"
                role="form"
                class="php-email-form"
              >
                <div class="row">
                  
                  <div class="form-group">
                    <label for="name">Class Title</label>
                    <input
                      type="text"
                      class="form-control"
                      name="subject"
                      id="subject"
                      required
                    />
                  </div>


                  <div class="form-group">
                    <label for="name">Class Size</label>
                    <input
                      type="text"
                      name="name"
                      class="form-control"
                      id="name"
                      required
                    />
                  </div>
                  
                  <div class="form-group">
                    <label for="name">Trainer Assigned</label>
                    <input
                      type="dropdown"
                      class="form-control"
                      name="email"
                      id="email"
                      required
                    />

                  <br>

                    <label for="cars">Assign a Trainer:</label>
                      <select name="cars" id="cars">
                        <optgroup label="Sales Department">
                          <option value="Halim">Halim</option>
                          <option value="Mark">Mark</option>
                        </optgroup>
                        <optgroup label="Leasing Department">
                          <option value="Bob">Bob</option>
                          <option value="Ali">Ali</option>
                        </optgroup>
                      </select>
                    
                  
                    
                  </div>
                    
                </div>

                
                <!-- <div class="form-group">
                  <label for="name">Message</label>
                  <textarea
                    class="form-control"
                    name="message"
                    rows="10"
                    required
                  ></textarea>
                </div>
                <div class="my-3">
                  <div class="loading">Loading</div>
                  <div class="error-message"></div>
                  <div class="sent-message">
                    Your message has been sent. Thank you!
                  </div>
                </div>
                <div class="text-center">
                  <button type="submit">Send Message</button>
                </div> -->
              </form>
              
            </div>


            <div class="col-lg-6 d-flex align-items-stretch">     
              <div class="info">
                <div>
                  <h5>Class Start Date: </h5>
                  <client-only>
                    <date-picker
                      placeholder="MM/DD/YYYY"
                      format="MM/dd/yyyy"
                      v-model="date_today" />
                  </client-only>
                  <div class="date">
                  <h5>Class End Date: </h5>
                  <client-only>
                    <date-picker
                      placeholder="MM/DD/YYYY"
                      format="MM/dd/yyyy"
                      v-model="date_today" />
                  </client-only>
                  </div>
                </div>
              </div>
                <div class="info">
                  <h5>Enrolment Start Date: </h5>
                  <client-only>
                    <date-picker
                      placeholder="MM/DD/YYYY"
                      format="MM/dd/yyyy"
                      v-model="date_today" />
                  </client-only>
                  <div class="date">
                    <h5>Enrolment End Date: </h5>
                    <client-only>
                      <date-picker
                        placeholder="MM/DD/YYYY"
                        format="MM/dd/yyyy"
                        v-model="date_today" />
                    </client-only>
                  </div>
                </div>  
              </div>




            
          </div>
        </div>





      </section>

      <div class="buttongroup">
        <div class="classCreate">
            <a href="#" class="classCreate-btn">Create Class</a>
        </div>
        <div class="cancel">
            <a href="ViewClasses" class="cancel-btn">Cancel</a>
        </div>
      </div>








    </div>


</template>

<script>
</script>
