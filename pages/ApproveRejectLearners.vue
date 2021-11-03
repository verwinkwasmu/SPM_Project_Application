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

            <b-tabs>
              <b-tab-item label="Table">
                  <b-table
                      :data="data"
                      :columns="columns"
                      :checked-rows.sync="checkedRows"
                      :is-row-checkable="(row) "
                      checkable
                      :checkbox-position="checkboxPosition">

                      <!-- <template #bottom-left>
                          <b>Total checked</b>: {{ checkedRows.length }}
                      </template> -->
                  </b-table>
              </b-tab-item>

          <div class="reject">
              <a href="" class="reject-btn">Reject</a>
          </div> <!-- Link to DB to refresh page with updated list-->

              <!-- <b-tab-item label="Checked rows">
                  <pre>{{ checkedRows }}</pre>
              </b-tab-item> -->
          </b-tabs>

            <div class="approve">
              <a href="" class="approve-btn" @click="ViewClasses">Approve</a>
            </div>
            <!-- Link to DB to refresh page with updated list-->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
      data() {
          const data = [
              { 'id': 1, 'engineer_name': 'Jesse Simmons'},
              { 'id': 2, 'engineer_name': 'John Jacobs'},
              { 'id': 3, 'engineer_name': 'Tina Gilbert'},
              { 'id': 4, 'engineer_name': 'Clarence Flores'},
              { 'id': 5, 'engineer_name': 'Anne Lee'}
          ]
          return {
              data,
              checkboxPosition: 'right',
              checkedRows: [],
              columns: [
                  {
                      field: 'id',
                      label: 'ID',
                      width: '40',
                      numeric: true
                  },
                  {
                      field: 'engineer_name',
                      label: 'Engineer Name',
                  }
              ]
          }
      }
  }
</script>  