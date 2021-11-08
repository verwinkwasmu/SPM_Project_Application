<template>
  <div>
    <section id="contact" class="contact">
        <div class="container">
          <div class="section-title">
            <h2>Log IN</h2>
          </div>
          <div class="row">
            <div class="col-lg-6" id="login">
              <div id="app" class="">
                    <div class="form-group">
                      <label for="name">Username: </label>
                      <input
                        v-model="userName"
                        type="text"
                        class="form-control"
                        name="subject"
                        id="subject"
                        required
                      />
                    </div>
                    <div class="form-group">
                      <button type="button" class="btn btn-primary" @click="login">Login</button>
                    </div>

              </div>

                <br />
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

            </div>
          </div>
        </div>
    </section>
  </div>
</template>


<script>
import axios from "axios";
export default {
  data: () => ({
    userName:"",
    error: null,
    message: "",
    data: null,
  }),
  methods: {
    async login(event) {
      event.preventDefault();
      if (!this.userName){
        this.error = true;
        this.message = "Please make sure userName is not empty!"
        return
      }
      const apiUrl = "https://spm-flask.herokuapp.com/login";
      const login_details = {
        userName: this.userName
      };
      try{
        let response = await axios.post(apiUrl, login_details)
        if (response.status == 200) {
              this.data = response.data;
              this.error = false;
              if (this.data.data.userType == 'HR'){
                localStorage.setItem('userId', this.data.data.userId)
                this.$router.push('/ViewCourses')
              }
              else if (this.data.data.userType == 'Learner'){
                localStorage.setItem('userId', this.data.data.userId)
                this.$router.push('/LearnerHomePage')
              }
              else if (this.data.data.userType == 'Trainer'){
                localStorage.setItem('userId', this.data.data.userId)
                this.$router.push('/TrainerHomePage')
              }
        } else {
              this.error = true;
              this.message = "Login Error. Please try again.";
        }
      }catch(err){
        console.log(err)
        this.error = true;
        this.message = "Login Error. Please try again."
      } 
      
    },
  },
};
</script>

