
"use strict";

let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let StartTrajectory = require('./StartTrajectory.js')
let SetPIDParams = require('./SetPIDParams.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let GoToIncremental = require('./GoToIncremental.js')
let SwitchToManual = require('./SwitchToManual.js')
let GetWaypoints = require('./GetWaypoints.js')
let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let ResetController = require('./ResetController.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let GetPIDParams = require('./GetPIDParams.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let Hold = require('./Hold.js')
let GoTo = require('./GoTo.js')
let AddWaypoint = require('./AddWaypoint.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let InitWaypointSet = require('./InitWaypointSet.js')

module.exports = {
  InitHelicalTrajectory: InitHelicalTrajectory,
  StartTrajectory: StartTrajectory,
  SetPIDParams: SetPIDParams,
  IsRunningTrajectory: IsRunningTrajectory,
  SetSMControllerParams: SetSMControllerParams,
  GoToIncremental: GoToIncremental,
  SwitchToManual: SwitchToManual,
  GetWaypoints: GetWaypoints,
  InitCircularTrajectory: InitCircularTrajectory,
  InitWaypointsFromFile: InitWaypointsFromFile,
  GetSMControllerParams: GetSMControllerParams,
  GetMBSMControllerParams: GetMBSMControllerParams,
  SetMBSMControllerParams: SetMBSMControllerParams,
  ResetController: ResetController,
  SwitchToAutomatic: SwitchToAutomatic,
  GetPIDParams: GetPIDParams,
  ClearWaypoints: ClearWaypoints,
  Hold: Hold,
  GoTo: GoTo,
  AddWaypoint: AddWaypoint,
  InitRectTrajectory: InitRectTrajectory,
  InitWaypointSet: InitWaypointSet,
};
