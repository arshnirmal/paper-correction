(function (t) {
  function e(e) {
    for (
      var s, o, r = e[0], c = e[1], l = e[2], d = 0, f = [];
      d < r.length;
      d++
    )
      (o = r[d]),
        Object.prototype.hasOwnProperty.call(i, o) && i[o] && f.push(i[o][0]),
        (i[o] = 0);
    for (s in c) Object.prototype.hasOwnProperty.call(c, s) && (t[s] = c[s]);
    u && u(e);
    while (f.length) f.shift()();
    return a.push.apply(a, l || []), n();
  }
  function n() {
    for (var t, e = 0; e < a.length; e++) {
      for (var n = a[e], s = !0, r = 1; r < n.length; r++) {
        var c = n[r];
        0 !== i[c] && (s = !1);
      }
      s && (a.splice(e--, 1), (t = o((o.s = n[0]))));
    }
    return t;
  }
  var s = {},
    i = { app: 0 },
    a = [];
  function o(e) {
    if (s[e]) return s[e].exports;
    var n = (s[e] = { i: e, l: !1, exports: {} });
    return t[e].call(n.exports, n, n.exports, o), (n.l = !0), n.exports;
  }
  (o.m = t),
    (o.c = s),
    (o.d = function (t, e, n) {
      o.o(t, e) || Object.defineProperty(t, e, { enumerable: !0, get: n });
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
      var n = Object.create(null);
      if (
        (o.r(n),
        Object.defineProperty(n, "default", { enumerable: !0, value: t }),
        2 & e && "string" != typeof t)
      )
        for (var s in t)
          o.d(
            n,
            s,
            function (e) {
              return t[e];
            }.bind(null, s)
          );
      return n;
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
    c = r.push.bind(r);
  (r.push = e), (r = r.slice());
  for (var l = 0; l < r.length; l++) e(r[l]);
  var u = c;
  a.push([0, "chunk-vendors"]), n();
})({
  0: function (t, e, n) {
    t.exports = n("56d7");
  },
  "00a8": function (t, e, n) {
    "use strict";
    var s = n("1c0c"),
      i = n.n(s);
    i.a;
  },
  "0115": function (t, e, n) {
    "use strict";
    var s = n("4758"),
      i = n.n(s);
    i.a;
  },
  "034f": function (t, e, n) {
    "use strict";
    var s = n("85ec"),
      i = n.n(s);
    i.a;
  },
  "199c": function (t, e) {},
  "1c0c": function (t, e, n) {},
  "23be": function (t, e, n) {
    "use strict";
    var s = n("199c"),
      i = n.n(s);
    e["default"] = i.a;
  },
  "396e": function (t, e, n) {
    "use strict";
    var s = function () {
        var t = this,
          e = t.$createElement,
          n = t._self._c || e;
        return n("b-container", { attrs: { fluid: "" } }, [
          n(
            "div",
            { attrs: { id: "app" } },
            [n("vue-progress-bar"), n("router-view")],
            1
          ),
        ]);
      },
      i = [];
    n.d(e, "a", function () {
      return s;
    }),
      n.d(e, "b", function () {
        return i;
      });
  },
  "3dfd": function (t, e, n) {
    "use strict";
    var s = n("396e"),
      i = n("23be"),
      a = (n("034f"), n("2877")),
      o = Object(a["a"])(i["default"], s["a"], s["b"], !1, null, null, null);
    e["default"] = o.exports;
  },
  4712: function (t, e, n) {},
  4758: function (t, e, n) {},
  "56d7": function (t, e, n) {
    "use strict";
    n.r(e);
    n("e260"), n("e6cf"), n("cca6"), n("a79d");
    var s = n("2b0e"),
      i = n("3dfd"),
      a = n("8c4f"),
      o = function () {
        var t = this,
          e = t.$createElement,
          n = t._self._c || e;
        return n("div", { attrs: { id: "app" } }, [
          t._m(0),
          n("div", { staticClass: "body-container-wrapper" }, [
            n("div", { staticClass: "body-container" }, [
              n("div", { staticClass: "page-center" }, [
                t.spin
                  ? n(
                      "div",
                      [
                        n("b-icon", {
                          staticStyle: { width: "120px", height: "120px" },
                          attrs: { icon: "cloud-download" },
                        }),
                        n("h1", [t._v("Results are ready!")]),
                        n(
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
                  : n(
                      "div",
                      [
                        n("b-spinner", { attrs: { label: "Spinning" } }),
                        n("h4", [t._v("Please wait..")]),
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
            n = t._self._c || e;
          return n("div", { staticClass: "header-container-wrapper" }, [
            n("div", { staticClass: "header-container" }, [
              n("div", { staticClass: "custom-header-bg" }, [
                n("div", { staticClass: "page-center" }, [
                  n("div", { staticClass: "logo" }, [t._v("Here you go!")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "footer-container-wrapper" }, [
            n(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                n("div", { staticClass: "custom-footer-bg" }, [
                  n("div", { staticClass: "footer" }, [
                    n("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      c = (n("d3b7"), n("3ca3"), n("ddb0"), n("2b3d"), n("bc3a")),
      l = n.n(c),
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
            l.a
              .get("http://127.0.0.1:5000/download", { responseType: "blob" })
              .then(function (t) {
                var e = window.URL.createObjectURL(new Blob([t.data])),
                  n = document.createElement("a");
                (n.href = e),
                  n.setAttribute("download", "Student_result.zip"),
                  document.body.appendChild(n),
                  n.click();
              })
              .catch(console.error),
              console.log(this.spin);
          },
        },
      },
      d = u,
      f = (n("00a8"), n("2877")),
      p = Object(f["a"])(d, o, r, !1, null, null, null),
      v = p.exports,
      h = function () {
        var t = this,
          e = t.$createElement,
          n = t._self._c || e;
        return n("div", { attrs: { id: "app" } }, [
          t._m(0),
          n("div", { staticClass: "body-container-wrapper" }, [
            n("div", { staticClass: "body-container" }, [
              n(
                "div",
                { staticClass: "page-center" },
                [
                  n("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  n("h1", [t._v("Upload Student Paper")]),
                  n(
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
                  n("router-link", { attrs: { to: "s2" } }, [
                    n(
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
                  n("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  n(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, s) {
                      return n("div", { key: s, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        n(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(s);
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
      m = [
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "header-container-wrapper" }, [
            n("div", { staticClass: "header-container" }, [
              n("div", { staticClass: "custom-header-bg" }, [
                n("div", { staticClass: "page-center" }, [
                  n("div", { staticClass: "logo" }, [t._v("Step 1")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "footer-container-wrapper" }, [
            n(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                n("div", { staticClass: "custom-footer-bg" }, [
                  n("div", { staticClass: "footer" }, [
                    n("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      b =
        (n("a434"),
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
                var n = this.files[e];
                t.append("file", n);
              }
              l.a
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
      _ = b,
      C = (n("0115"), Object(f["a"])(_, h, m, !1, null, null, null)),
      g = C.exports,
      y = function () {
        var t = this,
          e = t.$createElement,
          n = t._self._c || e;
        return n("div", { attrs: { id: "app" } }, [
          t._m(0),
          n("div", { staticClass: "body-container-wrapper" }, [
            n("div", { staticClass: "body-container" }, [
              n(
                "div",
                { staticClass: "page-center" },
                [
                  n("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  n("h1", [t._v("Upload Master Copy")]),
                  n(
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
                  n("router-link", { attrs: { to: "s3" } }, [
                    n(
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
                  n("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  n(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, s) {
                      return n("div", { key: s, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        n(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(s);
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
      w = [
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "header-container-wrapper" }, [
            n("div", { staticClass: "header-container" }, [
              n("div", { staticClass: "custom-header-bg" }, [
                n("div", { staticClass: "page-center" }, [
                  n("div", { staticClass: "logo" }, [t._v("Step 2")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "footer-container-wrapper" }, [
            n(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                n("div", { staticClass: "custom-footer-bg" }, [
                  n("div", { staticClass: "footer" }, [
                    n("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      x = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var n = this.files[e];
              t.append("master", n);
            }
            l.a
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
      F = x,
      S = (n("86a6"), Object(f["a"])(F, y, w, !1, null, null, null)),
      k = S.exports,
      $ = function () {
        var t = this,
          e = t.$createElement,
          n = t._self._c || e;
        return n("div", { attrs: { id: "app" } }, [
          t._m(0),
          n("div", { staticClass: "body-container-wrapper" }, [
            n("div", { staticClass: "body-container" }, [
              n(
                "div",
                { staticClass: "page-center" },
                [
                  n("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  n("h1", [
                    t._v("Upload Addtional files (for better correction)"),
                  ]),
                  n(
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
                  n("router-link", { attrs: { to: "results" } }, [
                    n(
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
                  n("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  n(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, s) {
                      return n("div", { key: s, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        n(
                          "span",
                          {
                            staticClass: "remove-file",
                            on: {
                              click: function (e) {
                                return t.removeFile(s);
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
      O = [
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "header-container-wrapper" }, [
            n("div", { staticClass: "header-container" }, [
              n("div", { staticClass: "custom-header-bg" }, [
                n("div", { staticClass: "page-center" }, [
                  n("div", { staticClass: "logo" }, [t._v("Step 3")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            n = t._self._c || e;
          return n("div", { staticClass: "footer-container-wrapper" }, [
            n(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                n("div", { staticClass: "custom-footer-bg" }, [
                  n("div", { staticClass: "footer" }, [
                    n("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      E = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var n = this.files[e];
              t.append("correction", n);
            }
            console.log(files.length),
              l.a
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
      j = E,
      P = (n("7985"), Object(f["a"])(j, $, O, !1, null, null, null)),
      U = P.exports;
    s["default"].use(a["a"]);
    var R = [
        { path: "/results", name: "download", component: v },
        { path: "/", name: "home", component: g },
        { path: "/s2", name: "step2", component: k },
        { path: "/s3", name: "step3", component: U },
      ],
      T = new a["a"]({ routes: R }),
      A = T,
      M = n("2f62");
    s["default"].use(M["a"]);
    var D = new M["a"].Store({
        state: {},
        mutations: {},
        actions: {},
        modules: {},
      }),
      Y = n("5f5b"),
      I = n("b1e0"),
      J = (n("f9e3"), n("2dd8"), n("3cb4")),
      K = n.n(J),
      L = n("26b9"),
      z = n.n(L),
      B = n("5132"),
      H = n.n(B);
    s["default"].component("Spinner", K.a);
    var q = {
      color: "#bffaf3",
      failedColor: "#874b4b",
      thickness: "2px",
      transition: { speed: "0.2s", opacity: "0.6s", termination: 300 },
      autoRevert: !0,
      location: "top",
      inverse: !1,
    };
    s["default"].use(z.a, q),
      s["default"].use(
        new H.a({
          debug: !0,
          connection: "",
          vuex: {
            store: D,
            actionPrefix: "SOCKET_",
            mutationPrefix: "SOCKET_",
          },
        })
      ),
      s["default"].use(Y["a"]),
      s["default"].use(I["a"]),
      (s["default"].config.productionTip = !1),
      new s["default"]({
        router: A,
        store: D,
        render: function (t) {
          return t(i["default"]);
        },
      }).$mount("#app");
  },
  "70ad": function (t, e, n) {},
  7985: function (t, e, n) {
    "use strict";
    var s = n("70ad"),
      i = n.n(s);
    i.a;
  },
  "85ec": function (t, e, n) {},
  "86a6": function (t, e, n) {
    "use strict";
    var s = n("4712"),
      i = n.n(s);
    i.a;
  },
});
//# sourceMappingURL=app.cefd8f54.js.map
