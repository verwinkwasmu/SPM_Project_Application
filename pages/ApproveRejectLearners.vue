<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div class="addEngineer">
              <h5>Pending list:</h5>
            </div>
            <div class="container" id="app">
            <div class="row">
                <div class="col-12">
                <table class="table table-bordered">
                    <thead>
                    <tr>
                        <th scope="col">Learner ID</th>
                        <th scope="col">Learner Name</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>{{learner3.learnerID}}</td>
                        <td>{{learner3.name}}</td>
                        <td>
                        <div class="custom-control custom-checkbox">
                            <input type="checkbox" class="custom-control-input" id="customCheck1" :value="learner3.learnerID" v-model="learnerName">
                            <label class="custom-control-label" for="customCheck1"></label>
                        </div>
                        </td>
                    </tr>
                    <tr>
                        <td>{{learner4.learnerID}}</td>
                        <td>{{learner4.name}}</td>
                        <td>
                        <div class="custom-control custom-checkbox">
                            <input type="checkbox" class="custom-control-input" id="customCheck2" :value="learner4.learnerID" v-model="learnerName">
                            <label class="custom-control-label" for="customCheck2"></label>
                        </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
                </div>
                {{learnerName}}
                <div class="ApproveRejectPage">
                    <div class="approve">
                        <a @click="submit" class="approve-btn">Approve</a>
                    </div>
                    <div class="reject">
                        <a href="" class="reject-btn">Reject</a>
                    </div> <!-- Link to DB to refresh page with updated list-->
              </div>
            </div>
              
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
    export default{
        name: 'app',
        data: () => ({
            name: '',
            learnerName: [],
            learner1: 'Ezboii',
            learner2: 'wxtohhh',

            learner3: {
                name: "hiii",
                learnerID: 10,
            },
            learner4: {
                name: "ooo",
                learnerID: 11,
            },
        }),

        methods: {
            submit () {
                
            }
        },

    }
</script>

