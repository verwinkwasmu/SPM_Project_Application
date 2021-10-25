<template>
  <div>
    <Header />
    <section id="team" class="team section-bg">
      <div class="container" data-aos="fade-up">
        <div class="row">
          <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
            <div class="addEngineer">
              <h5>Total List of Engineers:</h5>
            </div>

            <b-table
              :data="data"
              :columns="columns"
              :checked-rows.sync="checkedRows"
              checkable
              :checkbox-position="checkboxPosition"
            >
            </b-table>

            <div class="Add">
              <a href="" class="Add-btn" @click="enrolLearners">Add</a>
            </div>
            <!-- Link to DB to refresh page with updated list-->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    const data = [];

    return {
      data,
      checkboxPosition: "right",
      checkedRows: [],
      columns: [
        {
          field: "learnerId",
          label: "learnerId",
          width: "40",
          numeric: true,
        },
        {
          field: "learnerName",
          label: "learnerName",
        },
      ],
    };
  },
  async mounted() {
    const apiUrl = `http://localhost:5002/enrolment/qualifiedlearners/${this.$route.query.classId}`;
    try {
      let response = await axios.get(apiUrl);
      this.data = response.data.data;
      this.error = false;
    } catch (err) {
      console.log(err);
      this.error = true;
      this.message = err;
    }
  },
  methods: {
    async enrolLearners(event) {
      event.preventDefault();
      const apiUrl = `http://localhost:5002/enrolment`;
      const learnerIds = [];
      const checkedRows = this.checkedRows;

      checkedRows.forEach(function (arrayItem) {
        learnerIds.push(arrayItem.learnerId);
      });

      const enrolmentData = {
        classId: this.$route.query.classId,
        learnerIds: learnerIds,
      };

      try {
        let response = await axios.post(apiUrl, enrolmentData);
        if (response.status == 201) {
          alert("Successfully Enrolled!");
          window.location.reload();
        } else {
          alert("Please Try again!");
        }
      } catch (err) {
        console.log(err);
        this.error = true;
        this.message = err;
      }
    },
  },
};
</script>  
