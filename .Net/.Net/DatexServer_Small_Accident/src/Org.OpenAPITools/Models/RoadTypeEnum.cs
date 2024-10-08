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
        /// Gets or Sets RoadTypeEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<RoadTypeEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum RoadTypeEnum
        {
            
            /// <summary>
            /// Enum MotorwayEnum for motorway
            /// </summary>
            [EnumMember(Value = "motorway")]
            MotorwayEnum = 1,
            
            /// <summary>
            /// Enum TrunkRoadEnum for trunkRoad
            /// </summary>
            [EnumMember(Value = "trunkRoad")]
            TrunkRoadEnum = 2,
            
            /// <summary>
            /// Enum MainRoadEnum for mainRoad
            /// </summary>
            [EnumMember(Value = "mainRoad")]
            MainRoadEnum = 3,
            
            /// <summary>
            /// Enum OtherEnum for other
            /// </summary>
            [EnumMember(Value = "other")]
            OtherEnum = 4,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 5
        }
}
