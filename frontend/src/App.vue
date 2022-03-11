<template>
  <div class="container">
    <div class="main">
      <div class="logo">
        <img src="./assets/logo.png" alt="Blue Pages Logo">
      </div>
      <div class="form-and-results">
        <div class="form">
          <div class="form-title">
            <div class="title">Blue Pages helps you find anyone in seconds!</div>
            <div class="subtitle">Enter the fields below</div>
          </div>
          <div class="input-fields">
            <input v-model="firstName" type="text" placeholder="FIRST NAME">
            <input v-model="lastName" type="text" placeholder="LAST NAME">
            <select v-model="state">
              <option value="">STATE</option>
              <option 
                v-for="(state, index) in states" 
                :key="index" 
                :value="state.abbreviation">{{ state.name }}</option>
            </select>
            <button @click="search" class="search-btn">Search</button>
          </div>
        </div>
        <div class="results-container">
          <div class="results-title">Results</div>
          <div class="results">
            <div class="result" v-for="(item, index) in items" :key="index">
              <div class="result-col">
                <div class="result-col-title">
                  FIRST NAME
                </div>
                <div class="result-col-val">
                  {{ item.first_name }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  LAST NAME
                </div>
                <div class="result-col-val">
                  {{ item.last_name }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  STATE
                </div>
                <div class="result-col-val">
                  {{ item.state }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  PHONE NUMBER
                </div>
                <div class="result-col-val">
                  {{ item.phonenumber }}
                </div>
              </div>
            </div>
            <div v-if="items.length > 0" class="paging-container">
              <img @click="next()" src="./assets/arrow-left.svg">
              <span @click="selectPage(n)" v-for="n in numPages" :key=n v-bind:class="{ 'active-page': activePage === n }">{{n}}</span>
              <img @click="next()" src="./assets/arrow-right.svg">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

const API_URL = "http://localhost:8080";

export default {
  name: 'App',
  components: {},

  data() {
    return {
      firstName: "",
      lastName: "",
      state: "",
      states: [
        {"name":"Alabama","abbreviation":"AL"},
        {"name":"Alaska","abbreviation":"AK"},
        {"name":"Arizona","abbreviation":"AZ"},
        {"name":"Arkansas","abbreviation":"AR"},
        {"name":"California","abbreviation":"CA"},
        {"name":"Colorado","abbreviation":"CO"},
        {"name":"Connecticut","abbreviation":"CT"},
        {"name":"Delaware","abbreviation":"DE"},
        {"name":"District of Columbia","abbreviation":"DC"},
        {"name":"Florida","abbreviation":"FL"},
        {"name":"Georgia","abbreviation":"GA"},
        {"name":"Hawaii","abbreviation":"HI"},
        {"name":"Idaho","abbreviation":"ID"},
        {"name":"Illinois","abbreviation":"IL"},
        {"name":"Indiana","abbreviation":"IN"},
        {"name":"Iowa","abbreviation":"IA"},
        {"name":"Kansa","abbreviation":"KS"},
        {"name":"Kentucky","abbreviation":"KY"},
        {"name":"Lousiana","abbreviation":"LA"},
        {"name":"Maine","abbreviation":"ME"},
        {"name":"Maryland","abbreviation":"MD"},
        {"name":"Massachusetts","abbreviation":"MA"},
        {"name":"Michigan","abbreviation":"MI"},
        {"name":"Minnesota","abbreviation":"MN"},
        {"name":"Mississippi","abbreviation":"MS"},
        {"name":"Missouri","abbreviation":"MO"},
        {"name":"Montana","abbreviation":"MT"},
        {"name":"Nebraska","abbreviation":"NE"},
        {"name":"Nevada","abbreviation":"NV"},
        {"name":"New Hampshire","abbreviation":"NH"},
        {"name":"New Jersey","abbreviation":"NJ"},
        {"name":"New Mexico","abbreviation":"NM"},
        {"name":"New York","abbreviation":"NY"},
        {"name":"North Carolina","abbreviation":"NC"},
        {"name":"North Dakota","abbreviation":"ND"},
        {"name":"Ohio","abbreviation":"OH"},
        {"name":"Oklahoma","abbreviation":"OK"},
        {"name":"Oregon","abbreviation":"OR"},
        {"name":"Pennsylvania","abbreviation":"PA"},
        {"name":"Rhode Island","abbreviation":"RI"},
        {"name":"South Carolina","abbreviation":"SC"},
        {"name":"South Dakota","abbreviation":"SD"},
        {"name":"Tennessee","abbreviation":"TN"},
        {"name":"Texas","abbreviation":"TX"},
        {"name":"Utah","abbreviation":"UT"},
        {"name":"Vermont","abbreviation":"VT"},
        {"name":"Virginia","abbreviation":"VA"},
        {"name":"Washington","abbreviation":"WA"},
        {"name":"West Virginia","abbreviation":"WV"},
        {"name":"Wisconsin","abbreviation":"WI"},
        {"name":"Wyoming","abbreviation":"WY"}
      ],
      limit: 10,
      offset: 0,
      items: [],
      searchParams: {},
      result: {}
    };
  },

  methods: {
    async search() {
      this.searchParams = {
        firstName: this.firstName,
        lastName: this.lastName,
        state: this.state,
        limit: this.limit,
        offset: this.offset
      };

      const queryParams = new URLSearchParams(this.searchParams).toString();

      const request = await fetch(`${API_URL}/search/?${queryParams}`);

      if (!request.ok) {
        alert("Something went wrong while fetching the results");
        return;
      }
      this.result = await request.json();
      this.items = this.result.items;
      this.numPages = Math.ceil(this.result.total / this.result.count);
      this.activePage = 1;
    },
    async next() {
      if (this.searchParams.offset + this.searchParams.limit > this.result.total) {
        this.searchParams.offset = this.result.total - this.searchParams.limit;
      } else {
        this.searchParams.offset += this.searchParams.limit;
      }
      const queryParams = new URLSearchParams(this.searchParams).toString();
      const request = await fetch(`${API_URL}/search/?${queryParams}`);
      this.result = await request.json();
      this.items = this.result.items;
      this.activePage += 1;
    },
    async prev() {
      if (this.searchParams.offset - this.searchParams.limit < 0) {
        this.searchParams.offset = 0;
      } else {
        this.searchParams.offset -= this.searchParams.limit;
      }
      const queryParams = new URLSearchParams(this.searchParams).toString();
      const request = await fetch(`${API_URL}/search/?${queryParams}`);
      this.result = await request.json();
      this.items = this.result.items;
      this.activePage -= 1;
    },
    async selectPage(pageNum) {
      this.searchParams.offset = pageNum * this.searchParams.limit;
      const queryParams = new URLSearchParams(this.searchParams).toString();
      const request = await fetch(`${API_URL}/search/?${queryParams}`);
      this.result = await request.json();
      this.items = this.result.items;
      this.activePage = pageNum;
    }
  }
}
</script>

<style>
html, body { 
  --dark-blue: #3E6697;
  --light-blue: #E9F3FF;
  margin: 0; 
  padding: 0; 
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  height: 100%;
  color: var(--dark-blue);
  background-color: var(--light-blue);
}

.container {
  height: 100%;
  width: 100%;
}

.logo img {
  width: 200px;
}

.main {
  padding: 1rem 3rem;
}

.form-and-results {
  margin-top: 3%;
}

.form-title .title {
  font-weight: bold;
  font-size: 1rem;
}

.form-title .subtitle {
  font-size: 0.8rem;
  margin-top: 1rem;
}

.form .input-fields {
  margin-top: 1rem;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.input-fields > * {
  margin-top: 1rem;
}

.input-fields > input {
  /* Layout Properties */
  top: 232px;
  left: 42px;
  width: 309px;
  height: 53px;
  /* UI Properties */
  background: #FFFFFF 0% 0% no-repeat padding-box;
  border: 1px solid #3E6697;
  border-radius: 27px;
  opacity: 1;
}

.input-fields > select {
  /* https://stackoverflow.com/questions/611482/change-color-and-appearance-of-drop-down-arrow
    It is notoriously difficult to style a select component, such as the position or color of the caret.
    Better to use a third party component to replace the native select (e.g. https://ng-select.github.io/ng-select#/data-sources)
  */
  /* Layout Properties */
  top: 298px;
  left: 42px;
  width: 182px;
  height: 53px;
  /* UI Properties */
  background: #FFFFFF 0% 0% no-repeat padding-box;
  border: 1px solid #3E6697;
  border-radius: 27px;
  opacity: 1;
  /* UI Properties */
  text-align: left;
  font: normal normal medium 12px/16px Roboto;
  letter-spacing: 0px;
  color: #3E6697;
  opacity: 1;
}

.results > * {
  margin-top: 1rem;
}

.result {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  /* Layout Properties */
  /* top: 142px;
  left: 546px;
  width: 542px; */
  /* height: 65px; */
  /* UI Properties */
  background: #FFFFFF 0% 0% no-repeat padding-box;
  border: 1px solid #3E6697;
  opacity: 1;
}

.result-col-title {
  /* Layout Properties */
  /* top: 152px;
  left: 564px;
  width: 68px; */
  height: 16px;
  /* UI Properties */
  text-align: left;
  font: normal normal normal 12px/16px Roboto;
  letter-spacing: 0px;
  color: #3E6697;
  text-transform: uppercase;
  opacity: 1;
}

.result-col-val {
  /* Layout Properties */
  /* top: 176px;
  left: 564px;
  width: 39px; */
  height: 21px;
  /* UI Properties */
  text-align: left;
  font: normal normal normal 16px/21px Roboto;
  letter-spacing: 0px;
  color: #3E6697;
  opacity: 1;
}

::placeholder {
  /* UI Properties */
  text-align: left;
  font: normal normal medium 12px/16px Roboto;
  letter-spacing: 0px;
  color: #3E6697;
  opacity: 1;
}

.light-blue {
  color: #E9F3FF;
}

.dark-blue {
  color: #3E6697;
}

.active-page {
  font-weight: bold;
  text-decoration: underline;
}

.paging-container {
  text-align: center;
}

.paging-container > img {
  vertical-align: bottom;
  cursor: pointer;
}

.paging-container > span {
  margin: 0px 3px;
  display: inline-block;
  cursor: pointer;
}

.search-btn {
  /* Layout Properties */
  top: 398px;
  left: 242px;
  width: 109px;
  height: 47px;
  /* UI Properties */
  background: transparent url('./assets/blue.svg') 0% 0% no-repeat padding-box;
  opacity: 1;
  color: #FFFFFF;
}
</style>
