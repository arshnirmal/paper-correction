(function (t) {
  function e(e) {
    for (
      var n, r, o = e[0], l = e[1], c = e[2], f = 0, d = [];
      f < o.length;
      f++
    )
      (r = o[f]),
        Object.prototype.hasOwnProperty.call(s, r) && s[r] && d.push(s[r][0]),
        (s[r] = 0);
    for (n in l) Object.prototype.hasOwnProperty.call(l, n) && (t[n] = l[n]);
    u && u(e);
    while (d.length) d.shift()();
    return a.push.apply(a, c || []), i();
  }
  function i() {
    for (var t, e = 0; e < a.length; e++) {
      for (var i = a[e], n = !0, o = 1; o < i.length; o++) {
        var l = i[o];
        0 !== s[l] && (n = !1);
      }
      n && (a.splice(e--, 1), (t = r((r.s = i[0]))));
    }
    return t;
  }
  var n = {},
    s = { app: 0 },
    a = [];
  function r(e) {
    if (n[e]) return n[e].exports;
    var i = (n[e] = { i: e, l: !1, exports: {} });
    return t[e].call(i.exports, i, i.exports, r), (i.l = !0), i.exports;
  }
  (r.m = t),
    (r.c = n),
    (r.d = function (t, e, i) {
      r.o(t, e) || Object.defineProperty(t, e, { enumerable: !0, get: i });
    }),
    (r.r = function (t) {
      "undefined" !== typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(t, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(t, "__esModule", { value: !0 });
    }),
    (r.t = function (t, e) {
      if ((1 & e && (t = r(t)), 8 & e)) return t;
      if (4 & e && "object" === typeof t && t && t.__esModule) return t;
      var i = Object.create(null);
      if (
        (r.r(i),
        Object.defineProperty(i, "default", { enumerable: !0, value: t }),
        2 & e && "string" != typeof t)
      )
        for (var n in t)
          r.d(
            i,
            n,
            function (e) {
              return t[e];
            }.bind(null, n)
          );
      return i;
    }),
    (r.n = function (t) {
      var e =
        t && t.__esModule
          ? function () {
              return t["default"];
            }
          : function () {
              return t;
            };
      return r.d(e, "a", e), e;
    }),
    (r.o = function (t, e) {
      return Object.prototype.hasOwnProperty.call(t, e);
    }),
    (r.p = "/");
  var o = (window["webpackJsonp"] = window["webpackJsonp"] || []),
    l = o.push.bind(o);
  (o.push = e), (o = o.slice());
  for (var c = 0; c < o.length; c++) e(o[c]);
  var u = l;
  a.push([0, "chunk-vendors"]), i();
})({
  0: function (t, e, i) {
    t.exports = i("56d7");
  },
  "0115": function (t, e, i) {
    "use strict";
    var n = i("4758"),
      s = i.n(n);
    s.a;
  },
  "034f": function (t, e, i) {
    "use strict";
    var n = i("85ec"),
      s = i.n(n);
    s.a;
  },
  "199c": function (t, e) {},
  "23be": function (t, e, i) {
    "use strict";
    var n = i("199c"),
      s = i.n(n);
    e["default"] = s.a;
  },
  "396e": function (t, e, i) {
    "use strict";
    var n = function () {
        var t = this,
          e = t.$createElement,
          i = t._self._c || e;
        return i("b-container", { attrs: { fluid: "" } }, [
          i(
            "div",
            { attrs: { id: "app" } },
            [i("vue-progress-bar"), i("router-view")],
            1
          ),
        ]);
      },
      s = [];
    i.d(e, "a", function () {
      return n;
    }),
      i.d(e, "b", function () {
        return s;
      });
  },
  "3dfd": function (t, e, i) {
    "use strict";
    var n = i("396e"),
      s = i("23be"),
      a = (i("034f"), i("2877")),
      r = Object(a["a"])(s["default"], n["a"], n["b"], !1, null, null, null);
    e["default"] = r.exports;
  },
  4712: function (t, e, i) {},
  4758: function (t, e, i) {},
  "56d7": function (t, e, i) {
    "use strict";
    i.r(e);
    i("e260"), i("e6cf"), i("cca6"), i("a79d");
    var n = i("2b0e"),
      s = i("3dfd"),
      a = i("8c4f"),
      r = function () {
        var t = this,
          e = t.$createElement,
          i = t._self._c || e;
        return i("div", { attrs: { id: "app" } }, [
          t._m(0),
          i("div", { staticClass: "body-container-wrapper" }, [
            i("div", { staticClass: "body-container" }, [
              i(
                "div",
                { staticClass: "page-center" },
                [
                  i("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  i("h1", [t._v("Upload Student Paper")]),
                  i(
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
                  i("router-link", { attrs: { to: "s2" } }, [
                    i(
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
                  i("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  i(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return i("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        i(
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
      o = [
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "header-container-wrapper" }, [
            i("div", { staticClass: "header-container" }, [
              i("div", { staticClass: "custom-header-bg" }, [
                i("div", { staticClass: "page-center" }, [
                  i("div", { staticClass: "logo" }, [t._v("Step 1")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "footer-container-wrapper" }, [
            i(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                i("div", { staticClass: "custom-footer-bg" }, [
                  i("div", { staticClass: "footer" }, [
                    i("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      l = (i("a434"), i("bc3a")),
      c = i.n(l),
      u = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var i = this.files[e];
              t.append("file", i);
            }
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
      },
      f = u,
      d = (i("0115"), i("2877")),
      p = Object(d["a"])(f, r, o, !1, null, null, null),
      v = p.exports,
      h = function () {
        var t = this,
          e = t.$createElement,
          i = t._self._c || e;
        return i("div", { attrs: { id: "app" } }, [
          t._m(0),
          i("div", { staticClass: "body-container-wrapper" }, [
            i("div", { staticClass: "body-container" }, [
              i(
                "div",
                { staticClass: "page-center" },
                [
                  i("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  i("h1", [t._v("Upload Master Copy")]),
                  i(
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
                  i("router-link", { attrs: { to: "s3" } }, [
                    i(
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
                  i("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  i(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return i("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        i(
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
      m = [
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "header-container-wrapper" }, [
            i("div", { staticClass: "header-container" }, [
              i("div", { staticClass: "custom-header-bg" }, [
                i("div", { staticClass: "page-center" }, [
                  i("div", { staticClass: "logo" }, [t._v("Step 2")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "footer-container-wrapper" }, [
            i(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                i("div", { staticClass: "custom-footer-bg" }, [
                  i("div", { staticClass: "footer" }, [
                    i("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      b = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var i = this.files[e];
              t.append("master", i);
            }
            console.log(files.length),
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
      C = b,
      _ = (i("86a6"), Object(d["a"])(C, h, m, !1, null, null, null)),
      g = _.exports,
      y = function () {
        var t = this,
          e = t.$createElement,
          i = t._self._c || e;
        return i("div", { attrs: { id: "app" } }, [
          t._m(0),
          i("div", { staticClass: "body-container-wrapper" }, [
            i("div", { staticClass: "body-container" }, [
              i(
                "div",
                { staticClass: "page-center" },
                [
                  i("b-icon", {
                    staticStyle: { width: "120px", height: "120px" },
                    attrs: { icon: "cloud" },
                  }),
                  i("h1", [
                    t._v("Upload Addtional files (for better correction)"),
                  ]),
                  i(
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
                  i(
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
                  i("input", {
                    ref: "files",
                    attrs: { type: "file", id: "files", multiple: "" },
                    on: {
                      change: function (e) {
                        return t.handleFilesUpload();
                      },
                    },
                  }),
                  i(
                    "div",
                    { staticClass: "filesection" },
                    t._l(t.files, function (e, n) {
                      return i("div", { key: n, staticClass: "file-listing" }, [
                        t._v(" " + t._s(e.name) + " "),
                        i(
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
      w = [
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "header-container-wrapper" }, [
            i("div", { staticClass: "header-container" }, [
              i("div", { staticClass: "custom-header-bg" }, [
                i("div", { staticClass: "page-center" }, [
                  i("div", { staticClass: "logo" }, [t._v("Step 3")]),
                ]),
              ]),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i("div", { staticClass: "footer-container-wrapper" }, [
            i(
              "div",
              {
                staticClass: "footer-container",
                staticStyle: { "margin-top": "10px" },
              },
              [
                i("div", { staticClass: "custom-footer-bg" }, [
                  i("div", { staticClass: "footer" }, [
                    i("p", [t._v("@Roshni Magar")]),
                  ]),
                ]),
              ]
            ),
          ]);
        },
      ],
      F = {
        data: function () {
          return { files: [] };
        },
        methods: {
          addFiles: function () {
            this.$refs.files.click();
          },
          submitFiles: function () {
            for (var t = new FormData(), e = 0; e < this.files.length; e++) {
              var i = this.files[e];
              t.append("correction", i);
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
      x = F,
      S = (i("7985"), Object(d["a"])(x, y, w, !1, null, null, null)),
      k = S.exports;
    n["default"].use(a["a"]);
    var O = [
        { path: "/", name: "home", component: v },
        { path: "/s2", name: "step2", component: g },
        { path: "/s3", name: "step3", component: k },
      ],
      $ = new a["a"]({ routes: O }),
      j = $,
      P = i("2f62");
    n["default"].use(P["a"]);
    var E = new P["a"].Store({
        state: {},
        mutations: {},
        actions: {},
        modules: {},
      }),
      U = i("5f5b"),
      M = i("b1e0"),
      T = (i("f9e3"), i("2dd8"), i("e597")),
      A = i("26b9"),
      R = i.n(A),
      D = i("5132"),
      Y = i.n(D),
      J = i("8019");
    n["default"].component("file-upload", J);
    var K = {
      color: "#bffaf3",
      failedColor: "#874b4b",
      thickness: "2px",
      transition: { speed: "0.2s", opacity: "0.6s", termination: 300 },
      autoRevert: !0,
      location: "top",
      inverse: !1,
    };
    n["default"].use(R.a, K),
      n["default"].use(
        new Y.a({
          debug: !0,
          connection: "http://127.0.0.1:5000",
          vuex: {
            store: E,
            actionPrefix: "SOCKET_",
            mutationPrefix: "SOCKET_",
          },
        })
      ),
      n["default"].use(U["a"]),
      n["default"].use(M["a"]),
      (n["default"].config.productionTip = !1),
      n["default"].component("picture-input", T["a"]),
      new n["default"]({
        router: j,
        store: E,
        render: function (t) {
          return t(s["default"]);
        },
      }).$mount("#app");
  },
  "70ad": function (t, e, i) {},
  7985: function (t, e, i) {
    "use strict";
    var n = i("70ad"),
      s = i.n(n);
    s.a;
  },
  "85ec": function (t, e, i) {},
  "86a6": function (t, e, i) {
    "use strict";
    var n = i("4712"),
      s = i.n(n);
    s.a;
  },
});
//# sourceMappingURL=app.e025e27a.js.map
