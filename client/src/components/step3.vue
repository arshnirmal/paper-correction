<template>
  <div id="app">
    <div class="header-container-wrapper">
      <div class="header-container">
        <div class="custom-header-bg">
          <div class="page-center">
            <div class="logo">Step 3</div>
          </div>
        </div>
      </div>
    </div>

    <div class="body-container-wrapper">
      <div class="body-container">
        <div class="page-center">
          <b-icon icon="cloud" style="width:120px; height:120px;"></b-icon>
          <h1>Upload Addtional files (for better correction)</h1>
          <button class="samplebutton" v-on:click="addFiles()">Select Your Upload</button>
          <router-link :to="'results'">
            <button class="samplebutton" variant="success" v-on:click="submitFiles()">Submit</button>
          </router-link>
          <input type="file" id="files" ref="files" multiple v-on:change="handleFilesUpload()" />
          <div class="filesection">
            <div v-for="(file, key) in files" class="file-listing" v-bind:key="key">
              {{ file.name }}
              <span class="remove-file" v-on:click="removeFile(key)">Remove</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-container-wrapper">
      <div class="footer-container" style="margin-top: 10px;">
        <div class="custom-footer-bg">
          <div class="footer">
            <p>@Roshni Magar</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  /*
      Defines the data used by the component
    */
  data() {
    return {
      files: []
    };
  },

  /*
      Defines the method used by the component
    */
  methods: {
    /*
        Adds a file
      */
    addFiles() {
      this.$refs.files.click();
    },

    /*
        Submits files to the server
      */
    submitFiles() {
      /*
          Initialize the form data
        */
      let formData = new FormData();

      /*
          Iteate over any file sent over appending the files
          to the form data.
        */
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];

        formData.append("correction", file);
      }

      /*
          Make the request to the POST /select-files URL
        */
      console.log(files.length);
      axios
        .post("http://127.0.0.1:5000/correct-upload", formData)
        .then(response => {
          console.log("Files have been uploaded");
        })
        .catch(err => {
          console.error("Axios post error");
        });
    },

    /*
        Handles the uploading of files
      */
    handleFilesUpload() {
      let uploadedFiles = this.$refs.files.files;

      /*
          Adds the uploaded file to the files array
        */
      for (var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i]);
      }
    },

    /*
        Removes a select file the user has uploaded
      */
    removeFile(key) {
      this.files.splice(key, 1);
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i|Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i");
@-webkit-keyframes animation-rotate {
  100% {
    -webkit-transform: rotate(360deg);
  }
}

@-moz-keyframes animation-rotate {
  100% {
    -moz-transform: rotate(360deg);
  }
}

@-o-keyframes animation-rotate {
  100% {
    -o-transform: rotate(360deg);
  }
}

@keyframes animation-rotate {
  100% {
    transform: rotate(360deg);
  }
}

html {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
  font-family: "Raleway", sans-serif;
  transform: translateX(0%);
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  transition: transform 0.2s linear;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -o-user-select: none;
}
body.file-process-open {
  transform: translateX(-30%);
  transition: transform 0.2s linear;
}

* {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}

a {
  text-decoration: none;
}

h1 {
  font-family: "Open Sans", sans-serif;
  font-weight: 100;
  letter-spacing: 0px;
  font-size: 40px;
  line-height: 1.2;
}

.header-container .page-center,
.body-container .page-center,
.footer-container .page-center {
  margin: 0 auto;
  padding: 0 20px;
  overflow: hidden;
}
.button i {
  margin-right: 8px;
}
.header-container-wrapper {
  flex: 0 0 auto;
}
.body-container-wrapper {
  flex: 1 0 auto;
}
.footer-container-wrapper {
  flex: 0 0 auto;
  margin-bottom: 0px;
}
.body-container-wrapper.footer > *:last-child {
  margin-bottom: 0px;
  color: #fff;
}

.body-container-wrapper .page-center {
  display: flex;
  margin-bottom: 0px;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: calc(100vh - 170px);
}
.body-container i.fa.fa-cloud {
  font-size: 100px;
  color: #2196f3;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.48);
}
.custom-header-bg {
  background: #555;
  padding: 20px 0;
  font-family: "Open Sans", sans-serif;
  box-shadow: 0 0 12px #000;
}
.custom-footer-bg {
  background: #555;
  padding: 20px;
  text-align: center;
  color: #fff;
  box-shadow: 0 0 12px #000;
}
.logo {
  float: left;
  font-size: 24px;
  color: #ffffff;
  font-weight: 100;
  cursor: pointer;
  margin-top: 4px;
}

.navigation {
  float: right;
  width: 70%;
}

.navigation ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: block;
  float: right;
}

.navigation ul li {
  display: inline-block;
}

.button {
  white-space: nowrap;
  display: inline-block;
  height: 40px;
  line-height: 40px;
  padding: 0 30px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
  background: #fff;
  border-radius: 4px;
  font-size: 15px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  color: #555;
  text-decoration: none;
  -webkit-transition: all 0.15s ease;
  transition: all 0.15s ease;
  font-family: "Open Sans", sans-serif;
  font-weight: 400;
}

.button:hover {
  color: #6e6e6e;
  transform: translateY(-1px);
  box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}

.button:active {
  color: #555;
  background-color: #f6f9ff;
  transform: translateY(1px);
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}

.upload {
  padding: 0;
  background-color: #3498db;
  background-image: 8121991;
  background-image: -webkit-linear-gradient(#4aa3df 0%, #258cd1 100%);
  background-image: -moz-linear-gradient(#4aa3df 0%, #258cd1 100%);
  background-image: -o-linear-gradient(#4aa3df 0%, #258cd1 100%);
  background-image: linear-gradient(#4aa3df 0%, #258cd1 100%);
  -webkit-box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(52, 152, 219, 0.5) 0 0 5px;
  -moz-box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(52, 152, 219, 0.5) 0 0 5px;
  box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(52, 152, 219, 0.5) 0 0 5px;
  -webkit-border-radius: 4px;
  -webkit-background-clip: padding-box;
  -moz-border-radius: 4px;
  -moz-background-clip: padding;
  border-radius: 4px;
  background-clip: padding-box;
  padding: 20px 20px;
  color: #fff;
  cursor: pointer;
  font-weight: 600;
  font-family: Open Sans;
}

.upload span {
  text-shadow: rgba(29, 111, 165, 0.9) 0 0 2px;
}

.upload span {
  padding: 20px 25px;
  font: 700 13px Montserrat, Helvetica, Arial, sans-serif;
  text-transform: uppercase;
  color: #fff;
  -webkit-transition: all 350ms ease;
  -moz-transition: all 350ms ease;
  -o-transition: all 350ms ease;
  transition: all 350ms ease;
}

.upload:hover {
  background-color: #4aa3df;
  background-image: 8121991;
  background-image: -webkit-linear-gradient(#5faee3 0%, #3498db 100%);
  background-image: -moz-linear-gradient(#5faee3 0%, #3498db 100%);
  background-image: -o-linear-gradient(#5faee3 0%, #3498db 100%);
  background-image: linear-gradient(#5faee3 0%, #3498db 100%);
  -webkit-box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(74, 163, 223, 0.5) 0 0 5px;
  -moz-box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(74, 163, 223, 0.5) 0 0 5px;
  box-shadow: inset rgba(0, 0, 0, 0.2) 0 0 0 1px,
    rgba(74, 163, 223, 0.5) 0 0 5px;
}

.upload:hover span {
  text-shadow: rgba(33, 125, 187, 0.9) 0 0 2px;
}

.upload:active {
  background-color: #258cd1;
  background-image: 8121991;
  background-image: -webkit-linear-gradient(#258cd1 0%, #258cd1 100%);
  background-image: -moz-linear-gradient(#258cd1 0%, #258cd1 100%);
  background-image: -o-linear-gradient(#258cd1 0%, #258cd1 100%);
  background-image: linear-gradient(#258cd1 0%, #258cd1 100%);
}

.upload--loading {
  background-color: #258cd1 !important;
  background-image: 8121991 !important;
  background-image: -webkit-linear-gradient(
    #258cd1 0%,
    #258cd1 100%
  ) !important;
  background-image: -moz-linear-gradient(#258cd1 0%, #258cd1 100%) !important;
  background-image: -o-linear-gradient(#258cd1 0%, #258cd1 100%) !important;
  background-image: linear-gradient(#258cd1 0%, #258cd1 100%) !important;
  position: relative;
  cursor: wait;
}

.upload--loading:before {
  margin: -13px 0 0 -13px;
  width: 24px;
  height: 24px;
  position: absolute;
  left: 50%;
  top: 50%;
  content: "";
  -webkit-border-radius: 24px;
  -webkit-background-clip: padding-box;
  -moz-border-radius: 24px;
  -moz-background-clip: padding;
  border-radius: 24px;
  background-clip: padding-box;
  border: rgba(255, 255, 255, 0.25) 2px solid;
  border-top-color: #ffffff;
  -webkit-animation: animation-rotate 750ms linear infinite;
  -moz-animation: animation-rotate 750ms linear infinite;
  -o-animation: animation-rotate 750ms linear infinite;
  animation: animation-rotate 750ms linear infinite;
}

.upload--loading span,
.upload--loading:hover span,
.upload--loading:active span {
  color: transparent;
  text-shadow: none;
}

.upload-hidden {
  visibility: hidden;
}
.upload {
  position: relative;
  overflow: hidden;
}
.upload:after {
  content: "";
  position: absolute;
  top: -110%;
  left: -210%;
  width: 200%;
  height: 200%;
  opacity: 0;
  transform: rotate(30deg);
  background: rgba(255, 255, 255, 0.13);
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.13) 0%,
    rgba(255, 255, 255, 0.13) 77%,
    rgba(255, 255, 255, 0.5) 92%,
    rgba(255, 255, 255, 0) 100%
  );
}
.upload:hover:after {
  opacity: 1;
  top: -30%;
  left: 100%;
  transition-property: left, top, opacity;
  transition-duration: 0.7s, 0.7s, 0.15s;
  transition-timing-function: ease;
}
.upload:active:after {
  opacity: 0;
}
.file-upload-bar {
  height: 100%;
  position: fixed;
  right: -30%;
  width: 30%;
  top: 0;
  background: #2196f3;
  box-shadow: 0 0 22px #000;
  overflow: hidden;
  display: block;
  transition: all 0.2s linear;
}
.individual-files ul li:last-child {
  border: 0;
}
.file-process-open .file-upload-bar {
  right: 0;
  transition: all 0.2s linear;
  transform: translateX(100%);
}

.file-upload-bar-closed {
  position: fixed;
  right: -100%;
  height: 100vh;
  width: 70%;
  top: 0;
  cursor: pointer;
  transition: all 0.2s linear;
  z-index: 9999;
  transform: translateX(-30%);
}

.file-process-open .file-upload-bar-closed {
  transition: all 0.2s linear;
  transform: translateX(0%);
  right: 0;
  left: auto;
}
.bar-wrapper {
  padding: 20px;
}
.overall span {
  color: #fff;
  font-size: 20px;
  line-height: 1.2;
  font-weight: 300;
  background: #2196f3;
  display: inline-block;
  overflow: hidden;
  z-index: 9;
  position: relative;
  padding-right: 10px;
}
.overall {
  position: relative;
}
.overall:before {
  content: "";
  border-top: 2px solid #fff;
  height: 1px;
  width: 100%;
  position: absolute;
  top: 12px;
}
.progress-bar-overall {
  width: 100%;
  background: #fff;
  margin-top: 15px;
  height: 8px;
  transition: all 0.3s linear;
}
.progress-bar-overall span {
  background: #fff;
  color: #2196f3;
  padding: 5px 15px;
  transition: all 0.3s linear;
  position: relative;
  left: 10%;
  font-weight: bold;
  font-size: 15px;
  top: 8px;
  cursor: pointer;
  text-align: center;
}
.individual-files {
  border: 1px solid #fff;
  margin-top: 55px;
  padding: 0;
}
.individual-files ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
.individual-files ul li span {
  display: block;
  margin-bottom: 10px;
  font-family: "Open Sans", sans-serif;
  font-size: 13px;
}
.individual-files ul {
  height: calc(100vh - 160px);
  overflow-y: scroll;
  background: rgba(255, 255, 255, 1);
  background: -moz-linear-gradient(
    left,
    rgba(255, 255, 255, 1) 0%,
    rgba(246, 246, 246, 1) 47%,
    rgba(237, 237, 237, 1) 100%
  );
  background: -webkit-gradient(
    left top,
    right top,
    color-stop(0%, rgba(255, 255, 255, 1)),
    color-stop(47%, rgba(246, 246, 246, 1)),
    color-stop(100%, rgba(237, 237, 237, 1))
  );
  background: -webkit-linear-gradient(
    left,
    rgba(255, 255, 255, 1) 0%,
    rgba(246, 246, 246, 1) 47%,
    rgba(237, 237, 237, 1) 100%
  );
  background: -o-linear-gradient(
    left,
    rgba(255, 255, 255, 1) 0%,
    rgba(246, 246, 246, 1) 47%,
    rgba(237, 237, 237, 1) 100%
  );
  background: -ms-linear-gradient(
    left,
    rgba(255, 255, 255, 1) 0%,
    rgba(246, 246, 246, 1) 47%,
    rgba(237, 237, 237, 1) 100%
  );
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 1) 0%,
    rgba(246, 246, 246, 1) 47%,
    rgba(237, 237, 237, 1) 100%
  );
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ededed', GradientType=1 );
}
.individual-files ul li {
  padding: 10px;
  border-bottom: 1px solid #2196f3;
}
.individual-files ul li span i {
  font-style: normal;
  font-weight: bold;
  width: 80px;
  display: inline-block;
}
.individual-files ul li span b {
  font-weight: normal;
}
span.file-link input {
  padding: 5px 10px;
  border: none;
  background: transparent;
  outline: 0;
  padding-left: 0;
}
.copy-link b {
  background: #2196f3;
  padding: 5px 10px;
  display: inline-block;
  margin-left: 80px !important;
  cursor: pointer;
  color: #fff;
}
.copy-link b:active {
  background-color: rgba(33, 150, 243, 0.9);
  transform: translateY(1px);
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}
@media (max-width: 700px) {
  .custom-header-bg {
    text-align: center;
  }
  .logo {
    width: 100%;
    float: none;
    margin-bottom: 20px;
  }
  .navigation ul {
    float: none;
    text-align: center;
  }
  .navigation ul li + li {
    margin-top: 10px;
  }
  .navigation {
    float: none;
    width: 100%;
  }
}
.samplebutton {
  display: inline-block;
  margin: 7px; /* space between buttons */
  background: rgba(255, 255, 255, 0.075); /* background color */
  color: #2c3e50; /* text color */
  font-size: 1.2em;
  font-family: "Open Sans", sans-serif;
  border-width: 3px;
  border-color: #2c3e50;
  padding: 8px 16px; /* space around text */
  -moz-transition: all 0.2s;
  -webkit-transition: all 0.2s;
  transition: all 0.2s;
}
.samplebutton:hover {
  background: #555;
  color: #c1e1e0;
}

.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.fa-cloud:before {
  content: "\f0c2";
}
.i.fa.fa-cloud {
  font-size: 100px;
  color: #5a5f73;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.48);
}
</style>