(function (t) {
  function e(e) {
    for (
      var n, o, r = e[0], l = e[1], c = e[2], d = 0, f = [];
      d < r.length;
      d++
    )
      (o = r[d]),
        Object.prototype.hasOwnProperty.call(a, o) && a[o] && f.push(a[o][0]),
        (a[o] = 0);
    for (n in l) Object.prototype.hasOwnProperty.call(l, n) && (t[n] = l[n]);
    u && u(e);
    while (f.length) f.shift()();
    return i.push.apply(i, c || []), s();
  }
  function s() {
    for (var t, e = 0; e < i.length; e++) {
      for (var s = i[e], n = !0, r = 1; r < s.length; r++) {
        var l = s[r];
        0 !== a[l] && (n = !1);
      }
      n && (i.splice(e--, 1), (t = o((o.s = s[0]))));
    }
    return t;
  }
  var n = {},
    a = { app: 0 },
    i = [];
  function o(e) {
    if (n[e]) return n[e].exports;
    var s = (n[e] = { i: e, l: !1, exports: {} });
    return t[e].call(s.exports, s, s.exports, o), (s.l = !0), s.exports;
  }
  (o.m = t),
    (o.c = n),
    (o.d = function (t, e, s) {
      o.o(t, e) || Object.defineProperty(t, e, { enumerable: !0, get: s });
    }),
    (o.r = function (t) {
      "undefined" !== typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(t, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(t, "__esModule", { value: !0 });
    }),
    (o.t = function (t, e) {
      if ((1 & e && (t = o(t)), 8 & e)) return t;
      if (4 & e && "object" === typeof t && t && t.__esModule) return t;
      var s = Object.create(null);
      if (
        (o.r(s),
        Object.defineProperty(s, "default", { enumerable: !0, value: t }),
        2 & e && "string" != typeof t)
      )
        for (var n in t)
          o.d(
            s,
            n,
            function (e) {
              return t[e];
            }.bind(null, n)
          );
      return s;
    }),
    (o.n = function (t) {
      var e =
        t && t.__esModule
          ? function () {
              return t["default"];
            }
          : function () {
              return t;
            };
      return o.d(e, "a", e), e;
    }),
    (o.o = function (t, e) {
      return Object.prototype.hasOwnProperty.call(t, e);
    }),
    (o.p = "");
  var r = (window["webpackJsonp"] = window["webpackJsonp"] || []),
    l = r.push.bind(r);
  (r.push = e), (r = r.slice());
  for (var c = 0; c < r.length; c++) e(r[c]);
  var u = l;
  i.push([0, "chunk-vendors"]), s();
})({
  0: function (t, e, s) {
    t.exports = s("56d7");
  },
  "00a8": function (t, e, s) {
    "use strict";
    var n = s("1c0c"),
      a = s.n(n);
    a.a;
  },
  "0115": function (t, e, s) {
    "use strict";
    var n = s("4758"),
      a = s.n(n);
    a.a;
  },
  "034f": function (t, e, s) {
    "use strict";
    var n = s("85ec"),
      a = s.n(n);
    a.a;
  },
  "199c": function (t, e) {},
  "1c0c": function (t, e, s) {},
  "23be": function (t, e, s) {
    "use strict";
    var n = s("199c"),
      a = s.n(n);
    e["default"] = a.a;
  },
  "32d0": function (t, e, s) {
    "use strict";
    var n = s("3566"),
      a = s.n(n);
    a.a;
  },
  3566: function (t, e, s) {},
  "3dfd": function (t, e, s) {
    "use strict";
    var n = s("78fb"),
      a = s("23be"),
      i = (s("034f"), s("2877")),
      o = Object(i["a"])(a["default"], n["a"], n["b"], !1, null, null, null);
    e["default"] = o.exports;
  },
  4712: function (t, e, s) {},
  4758: function (t, e, s) {},
  "56d7": function (t, e, s) {
    "use strict";
    s.r(e);
    s("e260"), s("e6cf"), s("cca6"), s("a79d");
    var n = s("2b0e"),
      a = s("3dfd"),
      i = s("8c4f"),
      o = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s("div", { attrs: { id: "app" } }, [
          t._m(0),
          s("div", { staticClass: "body-container-wrapper" }, [
            s("div", { staticClass: "body-container" }, [
              s("div", { staticClass: "page-center" }, [
                t.spin
                  ? s(
                      "div",
                      [
                        s("b-icon", {
                          staticStyle: { width: "120px", height: "120px" },
                          attrs: { icon: "cloud-download" },
                        }),
                        s("h1", [t._v("Results are ready!")]),
                        s(
                          "button",
                          {
                            staticClass: "samplebutton",
                            attrs: { variant: "success" },
                            on: {
                              click: function (e) {
                                return t.downloadItem();
                              },
                            },
                          },
                          [t._v("Download")]
                        ),
                      ],
                      1
                    )
                  : t._e(),
                t.spin
                  ? t._e()
                  : s(
                      "div",
                      [
                        s("b-spinner", { attrs: { label: "Spinning" } }),
                        s("h4", [t._v("Please wait..")]),
                      ],
                      1
                    ),
              ]),
            ]),
          ]),
          t._m(1),
        ]);
      },
      r = [
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "header-container-wrapper" }, [
            s("div", { staticClass: "header-container" }, [
              s("div", { staticClass: "custom-header-bg" }, [
                s("div", { staticClass: "page-center" }, [
                  s("div", { staticClass: "logo" }, [t._v("Here you go!")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "footer-container-wrapper" }, [
            s(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                s("div", { staticClass: "custom-footer-bg" }, [
                  s("div", { staticClass: "footer" }, [
                    s("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      l = (s("d3b7"), s("3ca3"), s("ddb0"), s("2b3d"), s("bc3a")),
      c = s.n(l),
      u = {
        sockets: {
          connect: function () {
            console.log("connected");
          },
          text_response: function (t) {
            this.spin = t.data;
          },
        },
        data: function () {
          return { spin: "" };
        },
        methods: {
          downloadItem: function () {
            c.a
              .get("http://127.0.0.1:5000/download", { responseType: "blob" })
              .then(function (t) {
                var e = window.URL.createObjectURL(new Blob([t.data])),
                  s = document.createElement("a");
                (s.href = e),
                  s.setAttribute("download", "Student_result.zip"),
                  document.body.appendChild(s),
                  s.click();
              })
              .catch(console.error),
              console.log(this.spin);
          },
        },
      },
      d = u,
      f = (s("00a8"), s("2877")),
      p = Object(f["a"])(d, o, r, !1, null, null, null),
      v = p.exports,
      h = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s(
          "div",
          { attrs: { id: "test" } },
          [
            s(
              "b-navbar",
              { staticClass: "nav", attrs: { toggleable: "sm", type: "dark" } },
              [
                s(
                  "b-navbar",
                  { attrs: { variant: "faded", type: "light" } },
                  [
                    s(
                      "b-navbar-brand",
                      { staticClass: "mb-0", attrs: { tag: "h1" } },
                      [t._v("Automated paper correction")]
                    ),
                  ],
                  1
                ),
                s(
                  "b-navbar-nav",
                  { staticClass: "ml-auto" },
                  [
                    s(
                      "b-nav-item",
                      {
                        staticClass: "nav-items",
                        attrs: { id: "a", href: "#" },
                      },
                      [t._v("Docs")]
                    ),
                    s(
                      "b-nav-item",
                      {
                        staticClass: "nav-items",
                        attrs: { id: "a", href: "#" },
                      },
                      [t._v("About")]
                    ),
                  ],
                  1
                ),
              ],
              1
            ),
            s(
              "div",
              { staticClass: "mycontainer" },
              [
                s(
                  "b-overlay",
                  { attrs: { show: t.busy, opacity: 0.88, rounded: "sm" } },
                  [
                    t.step2 || t.step3 || t.step4
                      ? t._e()
                      : s(
                          "b-jumbotron",
                          { attrs: { id: "jumbo" } },
                          [
                            s("h1", [t._v("Step 1")]),
                            s("hr", { staticClass: "my-1" }),
                            s("b-icon", {
                              staticClass: "page-center",
                              staticStyle: { width: "120px", height: "120px" },
                              attrs: { icon: "cloud" },
                            }),
                            s("p", [
                              s("strong", [
                                t._v(
                                  " Please upload all the students answer here! "
                                ),
                              ]),
                            ]),
                            s(
                              "div",
                              [
                                s("file-pond", {
                                  ref: "student_file",
                                  attrs: {
                                    name: "file",
                                    "label-idle":
                                      "Drop files here or <span class='filepond--label-action'>Browse</span>",
                                    allowDrop: "true",
                                    allowMultiple: "true",
                                    instantUpload: "false",
                                    allowRevert: "True",
                                  },
                                }),
                              ],
                              1
                            ),
                            s(
                              "b-row",
                              { staticClass: "justify-content-md-center" },
                              [
                                s(
                                  "b-button",
                                  {
                                    attrs: { variant: "outline-dark" },
                                    on: { click: t.submitFiles },
                                  },
                                  [t._v("Upload files")]
                                ),
                              ],
                              1
                            ),
                          ],
                          1
                        ),
                    s(
                      "transition",
                      { attrs: { name: "slide" } },
                      [
                        !t.step2 || t.step3 || t.step4
                          ? t._e()
                          : s(
                              "b-jumbotron",
                              { attrs: { id: "jumbo" } },
                              [
                                s("h1", [t._v("Step 2")]),
                                s("hr", { staticClass: "my-1" }),
                                s("b-icon", {
                                  staticClass: "page-center",
                                  staticStyle: {
                                    width: "120px",
                                    height: "120px",
                                  },
                                  attrs: { icon: "cloud" },
                                }),
                                s("p", [
                                  s("strong", [
                                    t._v(" Please upload master copy! "),
                                  ]),
                                ]),
                                s(
                                  "div",
                                  [
                                    s("file-pond", {
                                      ref: "master_file",
                                      attrs: {
                                        name: "master_file",
                                        "label-idle":
                                          "Drop files here or <span class='filepond--label-action'>Browse</span>",
                                        allowDrop: "true",
                                        allowMultiple: "true",
                                        instantUpload: "false",
                                        allowRevert: "True",
                                      },
                                    }),
                                  ],
                                  1
                                ),
                                s(
                                  "b-row",
                                  { staticClass: "justify-content-md-center" },
                                  [
                                    s(
                                      "b-button",
                                      {
                                        attrs: { variant: "outline-dark" },
                                        on: { click: t.submitFilesmaster },
                                      },
                                      [t._v("Upload files")]
                                    ),
                                  ],
                                  1
                                ),
                              ],
                              1
                            ),
                      ],
                      1
                    ),
                    s(
                      "transition",
                      { attrs: { name: "slide" } },
                      [
                        t.step3 && !t.step4
                          ? s(
                              "b-jumbotron",
                              { attrs: { id: "jumbo" } },
                              [
                                s("h1", [t._v("Step 3")]),
                                s("hr", { staticClass: "my-1" }),
                                s("b-icon", {
                                  staticClass: "page-center",
                                  staticStyle: {
                                    width: "120px",
                                    height: "120px",
                                  },
                                  attrs: { icon: "cloud" },
                                }),
                                s("p", [
                                  s("strong", [
                                    t._v(
                                      " Please upload reference material here! "
                                    ),
                                  ]),
                                ]),
                                s(
                                  "div",
                                  [
                                    s("file-pond", {
                                      ref: "correct_file",
                                      attrs: {
                                        name: "correct_file",
                                        "label-idle":
                                          "Drop files here or <span class='filepond--label-action'>Browse</span>",
                                        allowDrop: "true",
                                        allowMultiple: "true",
                                        instantUpload: "false",
                                        allowRevert: "True",
                                      },
                                    }),
                                  ],
                                  1
                                ),
                                s(
                                  "b-row",
                                  { staticClass: "justify-content-md-center" },
                                  [
                                    s(
                                      "b-button",
                                      {
                                        attrs: { variant: "outline-dark" },
                                        on: { click: t.submitFilescorrect },
                                      },
                                      [t._v("Upload files")]
                                    ),
                                  ],
                                  1
                                ),
                              ],
                              1
                            )
                          : t._e(),
                      ],
                      1
                    ),
                    s(
                      "transition",
                      { attrs: { name: "slide" } },
                      [
                        t.step4
                          ? s(
                              "b-jumbotron",
                              { attrs: { id: "jumbo" } },
                              [
                                s("h1", [t._v("Download files")]),
                                s("hr", { staticClass: "my-1" }),
                                s("b-icon", {
                                  staticClass: "page-center mt-4",
                                  staticStyle: {
                                    width: "120px",
                                    height: "120px",
                                  },
                                  attrs: { icon: "cloud-download" },
                                }),
                                s("p", { staticClass: "mt-3" }, [
                                  s("strong", [
                                    t._v(" Click below to get results "),
                                  ]),
                                ]),
                                s(
                                  "b-row",
                                  { staticClass: "justify-content-md-center " },
                                  [
                                    s(
                                      "b-button",
                                      {
                                        staticClass: "mt-3",
                                        attrs: { variant: "dark" },
                                        on: { click: t.downloadItem },
                                      },
                                      [t._v("Download results")]
                                    ),
                                  ],
                                  1
                                ),
                              ],
                              1
                            )
                          : t._e(),
                      ],
                      1
                    ),
                  ],
                  1
                ),
              ],
              1
            ),
            s(
              "b-navbar",
              {
                staticClass: "nav",
                attrs: { toggleable: "sm", type: "dark", fixed: "bottom" },
              },
              [
                s(
                  "b-navbar-nav",
                  [s("b-nav-text", [s("strong", [t._v("@Roshni Magar")])])],
                  1
                ),
              ],
              1
            ),
          ],
          1
        );
      },
      m = [],
      b = (s("4160"), s("d81d"), s("0d03"), s("25f0"), s("159b"), s("1501")),
      _ = s.n(b),
      g = (s("4ed3"), s("a2d1"), s("57c8"), s("1942")),
      C = s.n(g),
      w = (s("7ec7"), _()(C.a)),
      y = {
        sockets: {
          connect: function () {
            console.log("connected");
          },
          text_response: function (t) {
            (this.busy = JSON.parse(t.data)),
              console.log("socketemit", this.busy);
          },
        },
        data: function () {
          return {
            stud_files: "",
            step2: !1,
            step3: !1,
            step4: !1,
            show: !1,
            busy: !1,
            timeout: null,
          };
        },
        methods: {
          clearTimeout: (function (t) {
            function e() {
              return t.apply(this, arguments);
            }
            return (
              (e.toString = function () {
                return t.toString();
              }),
              e
            );
          })(function () {
            this.timeout && (clearTimeout(this.timeout), (this.timeout = null));
          }),
          setTimeout: (function (t) {
            function e(e) {
              return t.apply(this, arguments);
            }
            return (
              (e.toString = function () {
                return t.toString();
              }),
              e
            );
          })(function (t) {
            var e = this;
            this.clearTimeout(),
              (this.timeout = setTimeout(function () {
                e.clearTimeout(), t();
              }, 1e3));
          }),
          submitFiles: function () {
            var t = this,
              e = new FormData();
            this.$refs.student_file
              .getFiles()
              .map(function (t) {
                return t.file;
              })
              .forEach(function (t) {
                e.append("file", t);
              }),
              c.a
                .post("http://127.0.0.1:5000/student-upload", e)
                .then(function (e) {
                  (t.busy = !0),
                    t.setTimeout(function () {
                      t.busy = !1;
                    }),
                    (t.step2 = !0),
                    console.log("Files have been uploaded"),
                    t.$refs.student_file.removeFiles();
                })
                .catch(function (t) {
                  console.error("Axios post error"), error("oh no");
                });
          },
          submitFilesmaster: function () {
            var t = this;
            (this.busy = !0),
              this.setTimeout(function () {
                t.busy = !1;
              });
            var e = new FormData();
            this.$refs.master_file
              .getFiles()
              .map(function (t) {
                return t.file;
              })
              .forEach(function (t) {
                e.append("master", t);
              }),
              c.a
                .post("http://127.0.0.1:5000/master-upload", e)
                .then(function (e) {
                  (t.step3 = !0),
                    (t.step2 = !1),
                    console.log("Files have been uploaded");
                })
                .catch(function (t) {
                  console.error("Axios post error");
                });
          },
          submitFilescorrect: function () {
            var t = this;
            this.busy = !0;
            var e = new FormData();
            this.$refs.correct_file
              .getFiles()
              .map(function (t) {
                return t.file;
              })
              .forEach(function (t) {
                e.append("correction", t);
              }),
              c.a
                .post("http://127.0.0.1:5000/correct-upload", e)
                .then(function (e) {
                  (t.step4 = !0),
                    (t.step3 = !1),
                    (t.step2 = !0),
                    console.log("Files have been uploaded");
                })
                .catch(function (t) {
                  console.error("Axios post error");
                });
          },
          downloadItem: function () {
            c.a
              .get("http://127.0.0.1:5000/download", { responseType: "blob" })
              .then(function (t) {
                var e = window.URL.createObjectURL(new Blob([t.data])),
                  s = document.createElement("a");
                (s.href = e),
                  s.setAttribute("download", "Student_result.zip"),
                  document.body.appendChild(s),
                  s.click();
              })
              .catch(console.error),
              console.log(this.spin);
          },
        },
        components: { FilePond: w },
      },
      F = y,
      x = (s("32d0"), Object(f["a"])(F, h, m, !1, null, null, null)),
      S = x.exports,
      k = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s("div", { attrs: { id: "app" } }, [
          t._m(0),
          s("div", { staticClass: "body-container-wrapper" }, [
            s("div", { staticClass: "body-container" }, [
              s(
                "div",
                { staticClass: "page-center" },
                [
                  s("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  s("h1", [t._v("Upload Student Paper")]),
                  s(
                    "button",
                    {
                      staticClass: "samplebutton",
                      on: {
                        click: function (e) {
                          return t.addFiles();
                        },
                      },
                    },
                    [t._v("Select Your Upload")]
                  ),
                  s("router-link", { attrs: { to: "s2" } }, [
                    s(
                      "button",
                      {
                        staticClass: "samplebutton",
                        attrs: { variant: "success" },
                        on: {
                          click: function (e) {
                            return t.submitFiles();
                          },
                        },
                      },
                      [t._v("Submit")]
                    ),
                  ]),
                  s("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  s(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return s("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        s(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(n);
                              },
                            },
                          },
                          [t._v("Remove")]
                        ),
                      ]);
                    }),
                    0
                  ),
                ],
                1
              ),
            ]),
          ]),
          t._m(1),
        ]);
      },
      j = [
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "header-container-wrapper" }, [
            s("div", { staticClass: "header-container" }, [
              s("div", { staticClass: "custom-header-bg" }, [
                s("div", { staticClass: "page-center" }, [
                  s("div", { staticClass: "logo" }, [t._v("Step 1")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "footer-container-wrapper" }, [
            s(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                s("div", { staticClass: "custom-footer-bg" }, [
                  s("div", { staticClass: "footer" }, [
                    s("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      $ =
        (s("a434"),
        {
          data: function () {
            return { files: [] };
          },
          methods: {
            addFiles: function () {
              this.$refs.files.click();
            },
            submitFiles: function () {
              for (var t = new FormData(), e = 0; e < this.files.length; e++) {
                var s = this.files[e];
                t.append("file", s);
              }
              console.log(t),
                c.a
                  .post("http://127.0.0.1:5000/student-upload", t)
                  .then(function (t) {
                    console.log("Files have been uploaded");
                  })
                  .catch(function (t) {
                    console.error("Axios post error");
                  });
            },
            handleFilesUpload: function () {
              for (var t = this.$refs.files.files, e = 0; e < t.length; e++)
                this.files.push(t[e]);
            },
            removeFile: function (t) {
              this.files.splice(t, 1);
            },
          },
        }),
      O = $,
      U = (s("0115"), Object(f["a"])(O, k, j, !1, null, null, null)),
      E = U.exports,
      P = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s("div", { attrs: { id: "app" } }, [
          t._m(0),
          s("div", { staticClass: "body-container-wrapper" }, [
            s("div", { staticClass: "body-container" }, [
              s(
                "div",
                { staticClass: "page-center" },
                [
                  s("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  s("h1", [t._v("Upload Master Copy")]),
                  s(
                    "button",
                    {
                      staticClass: "samplebutton",
                      on: {
                        click: function (e) {
                          return t.addFiles();
                        },
                      },
                    },
                    [t._v("Select Your Upload")]
                  ),
                  s("router-link", { attrs: { to: "s3" } }, [
                    s(
                      "button",
                      {
                        staticClass: "samplebutton",
                        attrs: { variant: "success" },
                        on: {
                          click: function (e) {
                            return t.submitFiles();
                          },
                        },
                      },
                      [t._v("Submit")]
                    ),
                  ]),
                  s("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  s(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return s("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        s(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(n);
                              },
                            },
                          },
                          [t._v("Remove")]
                        ),
                      ]);
                    }),
                    0
                  ),
                ],
                1
              ),
            ]),
          ]),
          t._m(1),
        ]);
      },
      T = [
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "header-container-wrapper" }, [
            s("div", { staticClass: "header-container" }, [
              s("div", { staticClass: "custom-header-bg" }, [
                s("div", { staticClass: "page-center" }, [
                  s("div", { staticClass: "logo" }, [t._v("Step 2")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "footer-container-wrapper" }, [
            s(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                s("div", { staticClass: "custom-footer-bg" }, [
                  s("div", { staticClass: "footer" }, [
                    s("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      D = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var s = this.files[e];
              t.append("master", s);
            }
            c.a
              .post("http://127.0.0.1:5000/master-upload", t)
              .then(function (t) {
                console.log("Files have been uploaded");
              })
              .catch(function (t) {
                console.error("Axios post error");
              });
          },
          handleFilesUpload: function () {
            for (var t = this.$refs.files.files, e = 0; e < t.length; e++)
              this.files.push(t[e]);
          },
          removeFile: function (t) {
            this.files.splice(t, 1);
          },
        },
      },
      A = D,
      R = (s("86a6"), Object(f["a"])(A, P, T, !1, null, null, null)),
      M = R.exports,
      B = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s("div", { attrs: { id: "app" } }, [
          t._m(0),
          s("div", { staticClass: "body-container-wrapper" }, [
            s("div", { staticClass: "body-container" }, [
              s(
                "div",
                { staticClass: "page-center" },
                [
                  s("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  s("h1", [
                    t._v("Upload Addtional files (for better correction)"),
                  ]),
                  s(
                    "button",
                    {
                      staticClass: "samplebutton",
                      on: {
                        click: function (e) {
                          return t.addFiles();
                        },
                      },
                    },
                    [t._v("Select Your Upload")]
                  ),
                  s("router-link", { attrs: { to: "results" } }, [
                    s(
                      "button",
                      {
                        staticClass: "samplebutton",
                        attrs: { variant: "success" },
                        on: {
                          click: function (e) {
                            return t.submitFiles();
                          },
                        },
                      },
                      [t._v("Submit")]
                    ),
                  ]),
                  s("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  s(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return s("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        s(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(n);
                              },
                            },
                          },
                          [t._v("Remove")]
                        ),
                      ]);
                    }),
                    0
                  ),
                ],
                1
              ),
            ]),
          ]),
          t._m(1),
        ]);
      },
      I = [
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "header-container-wrapper" }, [
            s("div", { staticClass: "header-container" }, [
              s("div", { staticClass: "custom-header-bg" }, [
                s("div", { staticClass: "page-center" }, [
                  s("div", { staticClass: "logo" }, [t._v("Step 3")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            s = t._self._c || e;
          return s("div", { staticClass: "footer-container-wrapper" }, [
            s(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                s("div", { staticClass: "custom-footer-bg" }, [
                  s("div", { staticClass: "footer" }, [
                    s("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      L = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var s = this.files[e];
              t.append("correction", s);
            }
            console.log(files.length),
              c.a
                .post("http://127.0.0.1:5000/correct-upload", t)
                .then(function (t) {
                  console.log("Files have been uploaded");
                })
                .catch(function (t) {
                  console.error("Axios post error");
                });
          },
          handleFilesUpload: function () {
            for (var t = this.$refs.files.files, e = 0; e < t.length; e++)
              this.files.push(t[e]);
          },
          removeFile: function (t) {
            this.files.splice(t, 1);
          },
        },
      },
      J = L,
      Y = (s("7985"), Object(f["a"])(J, B, I, !1, null, null, null)),
      z = Y.exports;
    n["default"].use(i["a"]);
    var K = [
        { path: "/results", name: "download", component: v },
        { path: "/", name: "test", component: S },
        { path: "/home", name: "home", component: E },
        { path: "/s2", name: "step2", component: M },
        { path: "/s3", name: "step3", component: z },
      ],
      H = new i["a"]({ routes: K }),
      N = H,
      q = s("2f62");
    n["default"].use(q["a"]);
    var G = new q["a"].Store({
        state: {},
        mutations: {},
        actions: {},
        modules: {},
      }),
      Q = s("5f5b"),
      V = s("b1e0"),
      W = (s("f9e3"), s("2dd8"), s("3cb4")),
      X = s.n(W),
      Z = s("5132"),
      tt = s.n(Z);
    n["default"].component("Spinner", X.a),
      n["default"].use(
        new tt.a({
          debug: !0,
          connection: "http://127.0.0.1:5000",
          vuex: {
            store: G,
            actionPrefix: "SOCKET_",
            mutationPrefix: "SOCKET_",
          },
        })
      ),
      n["default"].use(Q["a"]),
      n["default"].use(V["a"]),
      (n["default"].config.productionTip = !1);
    var et = s("f13c");
    n["default"].use(et),
      new n["default"]({
        router: N,
        store: G,
        render: function (t) {
          return t(a["default"]);
        },
      }).$mount("#app");
  },
  "70ad": function (t, e, s) {},
  "78fb": function (t, e, s) {
    "use strict";
    var n = function () {
        var t = this,
          e = t.$createElement,
          s = t._self._c || e;
        return s("b-container", { attrs: { fluid: "" } }, [
          s("div", { attrs: { id: "app" } }, [s("router-view")], 1),
        ]);
      },
      a = [];
    s.d(e, "a", function () {
      return n;
    }),
      s.d(e, "b", function () {
        return a;
      });
  },
  7985: function (t, e, s) {
    "use strict";
    var n = s("70ad"),
      a = s.n(n);
    a.a;
  },
  "85ec": function (t, e, s) {},
  "86a6": function (t, e, s) {
    "use strict";
    var n = s("4712"),
      a = s.n(n);
    a.a;
  },
  a2d1: function (t, e, s) {},
});
//# sourceMappingURL=app.6c5a8c15.js.map
