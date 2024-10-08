/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
        /// <summary>
        /// Gets or Sets CarriagewayEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<CarriagewayEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum CarriagewayEnum
        {
            
            /// <summary>
            /// Enum ConnectingCarriagewayEnum for connectingCarriageway
            /// </summary>
            [EnumMember(Value = "connectingCarriageway")]
            ConnectingCarriagewayEnum = 1,
            
            /// <summary>
            /// Enum CycleTrackEnum for cycleTrack
            /// </summary>
            [EnumMember(Value = "cycleTrack")]
            CycleTrackEnum = 2,
            
            /// <summary>
            /// Enum EntrySlipRoadEnum for entrySlipRoad
            /// </summary>
            [EnumMember(Value = "entrySlipRoad")]
            EntrySlipRoadEnum = 3,
            
            /// <summary>
            /// Enum ExitSlipRoadEnum for exitSlipRoad
            /// </summary>
            [EnumMember(Value = "exitSlipRoad")]
            ExitSlipRoadEnum = 4,
            
            /// <summary>
            /// Enum FlyoverEnum for flyover
            /// </summary>
            [EnumMember(Value = "flyover")]
            FlyoverEnum = 5,
            
            /// <summary>
            /// Enum FootpathEnum for footpath
            /// </summary>
            [EnumMember(Value = "footpath")]
            FootpathEnum = 6,
            
            /// <summary>
            /// Enum LeftHandParallelCarriagewayEnum for leftHandParallelCarriageway
            /// </summary>
            [EnumMember(Value = "leftHandParallelCarriageway")]
            LeftHandParallelCarriagewayEnum = 7,
            
            /// <summary>
            /// Enum LeftHandFeederRoadEnum for leftHandFeederRoad
            /// </summary>
            [EnumMember(Value = "leftHandFeederRoad")]
            LeftHandFeederRoadEnum = 8,
            
            /// <summary>
            /// Enum MainCarriagewayEnum for mainCarriageway
            /// </summary>
            [EnumMember(Value = "mainCarriageway")]
            MainCarriagewayEnum = 9,
            
            /// <summary>
            /// Enum OppositeCarriagewayEnum for oppositeCarriageway
            /// </summary>
            [EnumMember(Value = "oppositeCarriageway")]
            OppositeCarriagewayEnum = 10,
            
            /// <summary>
            /// Enum ParallelCarriagewayEnum for parallelCarriageway
            /// </summary>
            [EnumMember(Value = "parallelCarriageway")]
            ParallelCarriagewayEnum = 11,
            
            /// <summary>
            /// Enum RightHandFeederRoadEnum for rightHandFeederRoad
            /// </summary>
            [EnumMember(Value = "rightHandFeederRoad")]
            RightHandFeederRoadEnum = 12,
            
            /// <summary>
            /// Enum RightHandParallelCarriagewayEnum for rightHandParallelCarriageway
            /// </summary>
            [EnumMember(Value = "rightHandParallelCarriageway")]
            RightHandParallelCarriagewayEnum = 13,
            
            /// <summary>
            /// Enum RoundaboutEnum for roundabout
            /// </summary>
            [EnumMember(Value = "roundabout")]
            RoundaboutEnum = 14,
            
            /// <summary>
            /// Enum ServiceRoadEnum for serviceRoad
            /// </summary>
            [EnumMember(Value = "serviceRoad")]
            ServiceRoadEnum = 15,
            
            /// <summary>
            /// Enum SlipRoadsEnum for slipRoads
            /// </summary>
            [EnumMember(Value = "slipRoads")]
            SlipRoadsEnum = 16,
            
            /// <summary>
            /// Enum UnderpassEnum for underpass
            /// </summary>
            [EnumMember(Value = "underpass")]
            UnderpassEnum = 17,
            
            /// <summary>
            /// Enum UnspecifiedCarriagewayEnum for unspecifiedCarriageway
            /// </summary>
            [EnumMember(Value = "unspecifiedCarriageway")]
            UnspecifiedCarriagewayEnum = 18,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 19
        }
}
