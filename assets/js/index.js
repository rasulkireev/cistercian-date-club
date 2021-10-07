import '../css/tailwind.css'
import { Application } from "stimulus"
import { definitionsFromContext } from "stimulus/webpack-helpers"
import './web3-auth.js'

const application = Application.start()
const context = require.context("./controllers", true, /\.js$/)
application.load(definitionsFromContext(context))
