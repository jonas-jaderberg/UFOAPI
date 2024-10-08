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
        /// Gets or Sets ComparisonOperatorEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<ComparisonOperatorEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum ComparisonOperatorEnum
        {
            
            /// <summary>
            /// Enum EqualToEnum for equalTo
            /// </summary>
            [EnumMember(Value = "equalTo")]
            EqualToEnum = 1,
            
            /// <summary>
            /// Enum GreaterThanEnum for greaterThan
            /// </summary>
            [EnumMember(Value = "greaterThan")]
            GreaterThanEnum = 2,
            
            /// <summary>
            /// Enum GreaterThanOrEqualToEnum for greaterThanOrEqualTo
            /// </summary>
            [EnumMember(Value = "greaterThanOrEqualTo")]
            GreaterThanOrEqualToEnum = 3,
            
            /// <summary>
            /// Enum LessThanEnum for lessThan
            /// </summary>
            [EnumMember(Value = "lessThan")]
            LessThanEnum = 4,
            
            /// <summary>
            /// Enum LessThanOrEqualToEnum for lessThanOrEqualTo
            /// </summary>
            [EnumMember(Value = "lessThanOrEqualTo")]
            LessThanOrEqualToEnum = 5,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 6
        }
}
