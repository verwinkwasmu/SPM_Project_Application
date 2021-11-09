<template>
  <div>
    <TrainerHeader/>

    <!-- <Homepage/> -->
    <section id="contact" class="contact">
      <div class="container" data-aos="fade-up">
        
        <div class="row pb-5 mb-2 ml-0">
            <div class="viewSection">
              <router-link :to="{path: '/TrainerViewSection/', query: {classId: classObj.classId}}" class="btn btn-primary">Back to see all Sections</router-link>
            </div>
          </div>

        <div class="section-title">
          <h2>Create Section</h2>
        </div>
          
        <div class="row">
          <div class="col-lg-8" id="createSection">
            <form
              action="forms/contact.php"
              method="post"
              role="form"
              class="php-email-form"
            >
              <div class="row">
                
                <div class="form-group">
                  <label for="name">Section ID: </label>
                  <input
                    v-model="sectionId"
                    type="text"
                    class="form-control"
                    name="subject"
                    id="subject"
                    required
                  />
                </div>
                  
              </div>
            
            </form>
          
            
          </div>
            <div
              v-if="error == true"
              class="alert alert-danger alert-dismissible fade show"
              role="alert"
            >
              {{ message }}
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
              ></button>
            </div>
            <div
              v-else-if="error == false"
              class="alert alert-success alert-dismissible fade show"
              role="alert"
            >
              {{ message }}
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
              ></button>
            </div>


          
        </div>
      </div>

    </section>

    <div class="buttongroup">
      <div class="TrainerCreateSection">
        <a href="#" class="btn btn-success" style="margin-left: 1010px" @click="createSection">Create Section</a>
      </div>
     
    </div>


  </div>


</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    sectionId: "",
    classObj: {},
    course: {},
    error: null,
    message: "",
    data: null,
  }),
  async mounted() {
    const apiUrl = `https://spm-flask.herokuapp.com/getClass/${this.$route.query.classId}`;
    try {
      let response = await axios.get(apiUrl);

      console.log(response)

      this.classObj = await response.data;
  
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },

  methods: {
    async createSection(event) {
      event.preventDefault();
      this.error = null;
	  if (!this.sectionId){
		  this.error = true;
		  this.message = "Please make sure Section ID is not empty!"
		  return
	  }
      const apiUrl = "https://spm-flask.herokuapp.com/createSection";
      const section_details = {
        sectionId: this.sectionId,
        classId: this.classObj.classId,
        fileName: ""
      };
	  try{
		  let response = await axios.post(apiUrl, section_details)
		  console.log(response)
		  if (response.status == 201) {
            this.data = response.data;
            this.error = false;
            this.message = "Section Successfully Created! 😃";
          } else {
            this.error = true;
            this.message = "Section already exists!";
          }
	  }catch(err){
		  console.log(err)
		  this.error = true;
		  this.message = err
	  }
      
    },
  },
};
</script>